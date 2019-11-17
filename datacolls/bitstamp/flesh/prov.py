from typing import Optional

import websocket
from datetime import datetime
import json
from abc import ABC, abstractmethod
import settings
from influxdb import InfluxDBClient

from loguru import logger


class Channel(ABC):
    # Type of channel, in instance:
    # live_trades
    type: str = ""

    def __init__(self, prov: 'Collector', currency: str):
        self.prov: 'Collector' = prov
        self.currency: str = currency

    @abstractmethod
    def process(self, data: dict):
        pass

    def subscribe(self):
        subscr = {
            'event': 'bts:subscribe',
            'data': {
                'channel': self.name
            }
        }
        self.prov.ws.send(json.dumps(subscr))

    @property
    def name(self):
        return f'{self.type}_{self.currency}usd'


class LiveTrades(Channel):
    type: str = 'live_trades'

    def process(self, data: dict):
        time: datetime = datetime.fromtimestamp(float(data['timestamp'])/1e6)
        json_body = [
            {
                'measurement': self.name,
                'time': str(time),
                'tags': {
                    'currency': self.currency,
                    'type': self.type
                },
                'fields': {
                    'amount': data['amount'],
                    'price': data['price'],
                    'type': data['type'],
                }
            }
        ]

        self.prov.influx.write_points(json_body)


class Collector:
    def __init__(self):
        logger.info("Starting Bitstamp Data Collector.")
        self.url = settings.Bitstamp.URL

        logger.info("Connecting to influxdb.")
        self.influx = InfluxDBClient(host='influxdb',
                                     port=8086,
                                     username='root',
                                     password='root',
                                     database='bitstamp')
        self.influx.create_database('bitstamp')

        self.channels = []

        for curr in settings.Bitstamp.SUPPORTED_CURRENCIES:
            self.channels.append(LiveTrades(self, currency=curr))

        self._connect()

    def get_channel(self, name: str) -> Optional[Channel]:
        results = list(filter(lambda x: x.name == name, self.channels))
        if len(results) == 0:
            return None
        if len(results) > 1:
            raise RuntimeError(f'Duplicate channels ({name}) detected!')

        return results[0]

    def _connect(self):
        logger.info("Connecting to the websocket.")
        websocket.enableTrace(True)
        #"wss://ws.bitstamp.net"
        self.ws = websocket.WebSocketApp(self.url,
                                         on_message=lambda ws, msg: self._on_message(msg),
                                         on_close=lambda ws: self._on_close(),
                                         on_open=lambda ws: self._on_open(),
                                         on_error=lambda ws, error: self._on_error(error))

        self.ws.run_forever()

    def _on_message(self, msg: str):
        data = json.loads(msg)
        if data['event'] == 'bts:subscription_succeeded':
            return

        channel = self.get_channel(data['channel'])
        if channel:
            channel.process(data['data'])

    def _on_close(self):
        pass

    def _on_open(self):
        # subscrs = ['live_trades_btcusd',
        #            # 'live_orders_btcusd',
        #            'order_book_btcusd',
        #            'detail_order_book_btcusd',
        #            'diff_order_book_btcusd']
        for ch in self.channels:
            ch.subscribe()

    def _on_error(self, error: str):
        raise RuntimeError(error)


if __name__ == '__main__':
    prov = Collector()
