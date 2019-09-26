from click.testing import CliRunner

from core.management.commands import produce


def test_prode(db):
    produce.command(recording_path="data/record1.json")
