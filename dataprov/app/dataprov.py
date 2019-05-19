import ptcomm
import logging
import exchanges.bitstamp as bitstamp
from influx import Influx

from api import Api

logger = logging.getLogger(__name__)
ptcomm.logs.setup(logger, '/app/dataprov/logs/dataprov.log')

d
class DataProv(object):
    def __init__(self):
        self.influx = Influx()
        self.api = Api()

        self.api.start()

        #ex = bitstamp.ExchGwApiBitstamp()
        #ex.connect(ex.get_link())
        while True:
            continue

dp = DataProv()
