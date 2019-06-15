from marshmallow import Schema, fields, post_load
import json
import datetime
#{'event': 'trade', 'data': '{"amount": 1.30134317, "buy_order_id": 1812223058, "sell_order_id": 1812213127, "amount_str": "1.30134317", "price_str": "767.03", "timestamp": "1531081434", "price": 767.02999999999997, "type": 0, "id": 69777738}', 'channel': 'live_trades_bchusd'}


class OrderSchema(Schema):
    amount = fields.Float(requiered=True)
    price = fields.Float(requiered=True)
    type = fields.Integer(requiered=True)
    timestamp = fields.Integer(requiered=True)

    @post_load
    def to_(self, data):
        return ret

#input = {"amount": 1.30134317, "buy_order_id": 1812223058, "sell_order_id": 1812213127, "amount_str": "1.30134317", "price_str": "767.03", "timestamp": "1531081434", "price": 767.02999999999997, "type": 0, "id": 69777738}
#schema = Bitstamp()
#loaded = schema.load(input)
