import os
import subprocess

from kubernetes import client, config


def run(command: str) -> str:
    try:
        return subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode("utf-8").strip()
    except subprocess.CalledProcessError as e:
        output: str = e.stdout.decode('utf-8').strip()
        error_msg: str = f"Command \"{e.cmd}\" produced error ({output})"
        raise RuntimeError(error_msg)


config.load_kube_config(
    os.path.join(os.environ["HOME"], '.kube/config'))

kube = client.CoreV1Api()
