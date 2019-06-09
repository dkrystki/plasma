from influxdb import InfluxDBClient
import config

class InfluxHelper(object):

    @staticmethod
    def create_db_if_not_exist(name):
        conf = config.InfluxDb
        client = InfluxDBClient(conf.address, conf.port, conf.user, conf.password, database='_internal')
        client.create_database(name)

    @staticmethod
    def get_database(name):
        conf = config.InfluxDb
        database = InfluxDBClient(conf.address, conf.port, conf.user, conf.password, database=name)
        return database


class Database(object):
    def __init__(self, name):
        InfluxHelper.create_db_if_not_exist(name)
        self.client = InfluxHelper.get_database(name)
