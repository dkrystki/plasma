from influx import InfluxHelper


class Exchange(object):
    trades_serializer = None
    order_book_serializer = None

    def __init__(self, name):
        self.name = name
        self.client = InfluxHelper.get_database(self.name)
