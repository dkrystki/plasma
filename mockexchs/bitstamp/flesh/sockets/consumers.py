from typing import Dict, Any

from channels.generic.websocket import WebsocketConsumer
import json


class Consumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        data: Dict[str, Any] = json.loads(text_data)
        message = {
            "event": "bts:subscription_succeeded",
            "channel": data["data"]["channel"],
            "data": {}
        }

        self.send(text_data=json.dumps(message))
