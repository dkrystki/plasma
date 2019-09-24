from typing import Dict, Any

from channels.generic.websocket import WebsocketConsumer
from .models import Client
import json


class Consumer(WebsocketConsumer):
    def connect(self):
        Client.objects.create(channel=self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        Client.objects.filter(channel=self.channel_name).delete()
        pass

    def receive(self, text_data=None, bytes_data=None):
        data: Dict[str, Any] = json.loads(text_data)
        message = {
            "event": "bts:subscription_succeeded",
            "channel": data["data"]["channel"],
            "data": {}
        }

        self.send(text_data=json.dumps(message))
