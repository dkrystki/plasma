from typing import List

from django.conf import settings

import djclick as click
import websocket
import json


class Collector:
    def __init__(self, time: int, currencies: List[str]) -> None:
        self.time = time
        self.currencies = currencies

        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(settings.BITSTAMP_WS_URL,
                                         on_message=lambda ws, msg: self._on_message(msg),
                                         on_close=lambda ws: self._on_close(),
                                         on_open=lambda ws: self._on_open(),
                                         on_error=lambda ws, error: self._on_error(error))

        self.channels = ['live_trades',
                         'live_orders',
                         'order_book',
                         'detail_order_book',
                         'diff_order_book']

        self.data = dict()

    def start(self):
        self.ws.run_forever()

    def _on_message(self, msg: str):
        data: dict = json.loads(msg)
        if data['event'] == 'bts:subscription_succeeded':
            return

        self.data

    def _on_close(self):
        pass

    def _subscribe(self, channel: str, currency: str):
        subscr = {
            'event': 'bts:subscribe',
            'data': {
                'channel': f'{channel}_{currency}usd'
            }
        }
        self.ws.send(json.dumps(subscr))

    def _on_open(self):
        for c in self.currencies:
            for ch in self.channels:
                self._subscribe(ch, c)

    def _on_error(self, error: str):
        pass


@click.command()
@click.option("--time", type=int, default=10, help="How long the data will be collected for in minutes.")
@click.option("--curr", type=str, default='btc', help="What currencies will be collected.", multiple=True)
def command(time, curr):
    coll = Collector(time, curr)
    coll.start()
