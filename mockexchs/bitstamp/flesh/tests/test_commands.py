from core.management.commands import produce
from sockets.models import Client


def test_prod(db):
    Client.objects.create(channel="test_channel")

    produce.command(recording_path="data/record.json")
