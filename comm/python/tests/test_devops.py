import os

import pytest

from pathlib import Path

from plasma.comm.python.pl.devops import run, CommandError


class TestRun:
    @pytest.fixture(autouse=True)
    def setup(self, env):
        self.env = env

    def test_run_simple_echo(self, capsys):
        result = run('echo "test"')
        assert len(result) == 1
        assert result[0] == 'test'
        assert capsys.readouterr().out == ""

    def test_run_simple_echo_print(self, capsys):
        result = run('echo "test"', print_output=True)
        assert capsys.readouterr().out == "test\r\n"
        assert result[0] == 'test'

    def test_run_multiple_results(self, capsys):
        result = run("""
        export VAR1=123
        echo "test"
        echo "test$VAR1"
        """)
        assert len(result) == 2
        assert result[0] == 'test'
        assert result[1] == 'test123'

        assert capsys.readouterr().out == ""

    def test_exceptions(self):
        with pytest.raises(CommandError) as e:
            run("""
                echo "test1"
                echo "throws error" && missing_command
                echo "test2"
                """)

        assert "missing_command: command not found" in str(e.value)

    def test_multine_command(self):
        result = run(""" 
                export VAR1=123
                echo "test \\ 
                blabla"
                echo "test\\
                 $VAR1"
                """)
        assert len(result) == 2
        assert result[0] == 'test blabla'
        assert result[1] == 'test123'

    def test_ignore_errors(self):
        result = run("""non_existend_command""", ignore_errors=True)
        assert len(result) == 1
        assert "non_existend_command: command not found" in result[0]


def test_shell(env):
    os.chdir(str(env.monorepo_root))
    run("./shell.py --dry-run")
    run("./shell.py --dry-run --save")

    assert Path(".env").exists()

    Path(".env").unlink()
