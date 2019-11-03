from pathlib import Path
from typing import List, Dict, Any
from tqdm import tqdm

from django.conf import settings
from channels.layers import get_channel_layer

import djclick as click
import websocket
import json

from sockets.models import Client
from asgiref.sync import async_to_sync


class Producer:
    def __init__(self, recording_path: str) -> None:
        self.recording_filename: Path = Path(recording_path)
        # self.progressbar: tqdm = tqdm(total=self.record_time, ncols=100)

    def start(self):
        content: Dict[str, Any] = json.loads(self.recording_filename.read_text())
        channel_layer = get_channel_layer()

        for event in content:
            async_to_sync(channel_layer.send)(Client.objects.last().channel, {
                "type": "chat.message",
                "text": event["payload"]
            })
        a = 1
        # self.timer.start()
        # self.ws.run_forever()


@click.command()
@click.option("--recording_path", type=str, help="Which recording to start producing.")
def command(recording_path):
    coll = Producer(recording_path)
    coll.start()
