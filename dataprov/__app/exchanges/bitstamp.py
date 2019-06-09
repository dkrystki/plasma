from ws_api_socket import  WebSocketApiClient
from BitcoinExchangeFH.befh.market_data import L2Depth, Trade
from BitcoinExchangeFH.befh.instrument import Instrument
from BitcoinExchangeFH.befh.util import Logger
import time
import threading
import json
from functools import partial
from datetime import datetime


class ExchGwApiBitstamp(WebSocketApiClient):
    """
    Exchange socket
    """
    def __init__(self):
        WebSocketApiClient.__init__(self, 'Bitstamp')

    @classmethod
    def get_trades_timestamp_field_name(cls):
        return 'timestamp'

    @classmethod
    def get_bids_field_name(cls):
        return 'bids'

    @classmethod
    def get_asks_field_name(cls):
        return 'asks'

    @classmethod
    def get_trade_side_field_name(cls):
        return 'type'

    @classmethod
    def get_trade_id_field_name(cls):
        return 'id'

    @classmethod
    def get_trade_price_field_name(cls):
        return 'price'

    @classmethod
    def get_trade_volume_field_name(cls):
        return 'amount'

    @classmethod
    def get_link(cls):
        return 'ws://ws.pusherapp.com/app/de504dc5763aeef9ff52?protocol=7'

    @classmethod
    def get_order_book_subscription_string(cls, instmt):
        if cls.is_default_instmt(instmt):
            return json.dumps({"event":"pusher:subscribe","data":{"channel":"order_book"}})
        else:
            return json.dumps({"event":"pusher:subscribe","data":{"channel":"order_book_%s" % instmt.get_instmt_code()}})

    @classmethod
    def get_trades_subscription_string(cls):
        if cls.is_default_instmt(instmt):
            return json.dumps({"event":"pusher:subscribe","data":{"channel":"live_trades"}})

    @classmethod
    def is_default_instmt(cls, instmt):
        return instmt.get_instmt_code() == "\"\"" or instmt.get_instmt_code() == "" or instmt.get_instmt_code() == "''"

    @classmethod
    def parse_l2_depth(cls, instmt, raw):
        """
        Parse raw data to L2 depth
        :param instmt: Instrument
        :param raw: Raw data in JSON
        """
        l2_depth = instmt.get_l2_depth()
        keys = list(raw.keys())
        if cls.get_bids_field_name() in keys and \
           cls.get_asks_field_name() in keys:

            # Date time
            l2_depth.date_time = datetime.utcnow().strftime("%Y%m%d %H:%M:%S.%f")

            # Bids
            bids = raw[cls.get_bids_field_name()]
            bids_len = min(l2_depth.depth, len(bids))
            for i in range(0, bids_len):
                l2_depth.bids[i].price = float(bids[i][0]) if not isinstance(bids[i][0], float) else bids[i][0]
                l2_depth.bids[i].volume = float(bids[i][1]) if not isinstance(bids[i][1], float) else bids[i][1]

            # Asks
            asks = raw[cls.get_asks_field_name()]
            asks_len = min(l2_depth.depth, len(asks))
            for i in range(0, asks_len):
                l2_depth.asks[i].price = float(asks[i][0]) if not isinstance(asks[i][0], float) else asks[i][0]
                l2_depth.asks[i].volume = float(asks[i][1]) if not isinstance(asks[i][1], float) else asks[i][1]
        else:
            raise Exception('Does not contain order book keys in instmt %s-%s.\nOriginal:\n%s' % \
                (instmt.get_exchange_name(), instmt.get_instmt_name(), \
                 raw))

        return l2_depth

    @classmethod
    def parse_trade(cls, instmt, raw):
        """
        :param instmt: Instrument
        :param raw: Raw data in JSON
        :return:
        """
        trade = Trade()
        keys = list(raw.keys())

        if cls.get_trades_timestamp_field_name() in keys and \
           cls.get_trade_id_field_name() in keys and \
           cls.get_trade_side_field_name() in keys and \
           cls.get_trade_price_field_name() in keys and \
           cls.get_trade_volume_field_name() in keys:

            # Date time
            date_time = float(raw[cls.get_trades_timestamp_field_name()])
            trade.date_time = datetime.utcfromtimestamp(date_time).strftime("%Y%m%d %H:%M:%S.%f")

            # Trade side
            # Buy = 0
            # Side = 1
            trade.trade_side = Trade.parse_side(raw[cls.get_trade_side_field_name()] + 1)

            # Trade id
            trade.trade_id = str(raw[cls.get_trade_id_field_name()])

            # Trade price
            trade.trade_price = raw[cls.get_trade_price_field_name()]

            # Trade volume
            trade.trade_volume = raw[cls.get_trade_volume_field_name()]
        else:
            raise Exception('Does not contain trade keys in instmt %s-%s.\nOriginal:\n%s' % \
                (instmt.get_exchange_name(), instmt.get_instmt_name(), \
                 raw))

        return trade
