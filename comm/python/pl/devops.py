import os
import re
import sys
from getpass import getpass
from typing import List, Optional

import pexpect
from loguru import logger


import environ
from tqdm import tqdm

environ = environ.Env()


class CommandError(RuntimeError):
    pass


class CustomPrint:
    def __init__(self, prompt: str, command: str):
        self.old_stdout = sys.stdout
        self.command = command
        self.prompt = prompt

    def write(self, text: bytes):
        text: str = text.decode("utf-8")

        for line in text.splitlines(keepends=True):
            if len(text) == 0:
                return

            if not any((s in line) for s in [self.command, self.prompt]):
                self.old_stdout.write(line)

    def flush(self):
        self.old_stdout.flush()


def run(command: str, ignore_errors: bool = False, print_output: bool = False, progress_bar: bool = False) -> List[str]:
    # preprocess
    # join multilines
    command = re.sub(r"\\(?:\t| )*\n(?:\t| )*", "", command)

    commands: List[str] = [s.strip() for s in command.splitlines() if s.strip()]

    rets: List[str] = []

    prompt = r"##PL_PROMPT##"

    p = pexpect.spawn("bash --rcfile /dev/null", env=os.environ, echo=False)
    p.delaybeforesend = None

    p.expect(r"(\$|#)")
    p.sendline(f"export PS1={prompt}")
    p.expect(prompt)

    # Get sudo password if needed
    if "sudo " in command:
        tries = 3
        while True:
            sudo_password = getpass("Sudo password: ")
            p.sendline('sudo echo "granting sudo"')
            p.sendline(sudo_password)
            try:
                p.expect(prompt, timeout=1)
                print("Thank you.")
            except pexpect.exceptions.TIMEOUT:
                tries -= 1

                if tries == 0:
                    print("sudo: 3 incorrect password attempts")
                    exit(1)

                print("Sorry, try again.")
                continue
            break

    pbar: Optional[tqdm] = None
    if progress_bar:
        pbar = tqdm(total=len(commands))

    for c in commands:
        if "PL_DEBUG" in environ:
            logger.debug(c)

        if print_output:
            p.logfile = CustomPrint(command=c, prompt=prompt)
        p.sendline(c)
        p.expect(prompt, timeout=60 * 15)
        if print_output:
            p.logfile = None

        raw_outputs: List[bytes] = p.before.splitlines()
        outputs: List[str] = [s.decode("utf-8").strip() for s in raw_outputs]
        # get exit code
        p.sendline('echo "$?"')
        p.expect(prompt)
        ret_code = int(p.before.splitlines()[0].strip())

        ret = ""
        if outputs:
            ret = "\n".join(outputs)
            rets.append(ret)

        if not ignore_errors:
            if ret_code != 0:
                raise CommandError(ret)

        if progress_bar:
            pbar.update(1)

    if progress_bar:
        pbar.close()

    return rets


