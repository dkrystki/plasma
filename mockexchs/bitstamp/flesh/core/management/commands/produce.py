from typing import List
from tqdm import tqdm

from django.conf import settings

import djclick as click
import websocket
import json
from shengren.timer import Timer
from datetime import datetime


class Producer:
    def __init__(self, record_time: int, currencies: List[str]) -> None:
        self.record_time = record_time
        self.currencies = currencies

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

        self.data = []
        self.timer: Timer = Timer()

        self.progressbar: tqdm = tqdm(total=self.record_time, ncols=100)

    def start(self):
        self.timer.start()
        self.ws.run_forever()

    def _on_message(self, msg: str):
        # subtraction of self.progressbar.n let it work in percent mode
        self.progressbar.update(round(self.timer.get(), 4)-self.progressbar.n)

        data: dict = json.loads(msg)
        if data['event'] == 'bts:subscription_succeeded':
            return

        event = {
            'time': self.timer.get(),
            'payload': data
        }
        self.data.append(event)

        if self.timer.get() >= self.record_time:
            self.ws.close()

    def _on_close(self):
        json_dump: str = json.dumps(self.data,  indent=4, sort_keys=True)

        filename: str = datetime.now().strftime(f'%Y-%m-%d_%H:%M:%S_R{self.record_time}')
        with (settings.RECORDINGS_DIR/f'{filename}.json').open('w') as f:
            f.write(json_dump)

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
        click.secho(error, fg='red')
        pass


@click.command()
@click.option("--recording_name", type=str, help="Which recording to start producing.")
def command(record_time):
    coll = Collector(record_time, curr)
    coll.start()
