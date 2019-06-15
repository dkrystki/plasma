from BitcoinExchangeFH.befh.api_socket import ApiSocket
import websocket
import threading
import json
import time
import zlib
import logging

logger = logging.getLogger(__name__)


class WebSocketApiClient(ApiSocket):
    """
    Generic REST API call
    """
    def __init__(self, id, received_data_compressed=False):
        """
        Constructor
        :param id: Socket id
        """
        ApiSocket.__init__(self)
        self.ws = None              # Web socket
        self.id = id
        self.wst = None             # Web socket thread
        self._connecting = False
        self._connected = False
        self._received_data_compressed = received_data_compressed
        self.on_message_handlers = []
        self.on_open_handlers = []
        self.on_close_handlers = []
        self.on_error_handlers = []

    def connect(self, url,
                on_message_handler=None,
                on_open_handler=None,
                on_close_handler=None,
                on_error_handler=None,
                reconnect_interval=10):
        """
        :param url: Url link
        :param on_message_handler: Message handler which take the message as
                           the first argument
        :param on_open_handler: Socket open handler which take the socket as
                           the first argument
        :param on_close_handler: Socket close handler which take the socket as
                           the first argument
        :param on_error_handler: Socket error handler which take the socket as
                           the first argument and the error as the second
                           argument
        :param reconnect_interval: The time interval for reconnection
        """
        logger.info("Connecting to socket <%s>..." % self.id)
        if on_message_handler is not None:
            self.on_message_handlers.append(on_message_handler)
        if on_open_handler is not None:
            self.on_open_handlers.append(on_open_handler)
        if on_close_handler is not None:
            self.on_close_handlers.append(on_close_handler)
        if on_error_handler is not None:
            self.on_error_handlers.append(on_error_handler)

        if not self._connecting and not self._connected:
            self._connecting = True
            self.ws = websocket.WebSocketApp(url,
                                             on_message=self.__on_message,
                                             on_close=self.__on_close,
                                             on_open=self.__on_open,
                                             on_error=self.__on_error)
            self.wst = threading.Thread(target=lambda: self.__start(reconnect_interval=reconnect_interval))
            self.wst.start()
            import time
            time.sleep(1)

            self.ws.send(json.dumps({"event":"pusher:subscribe","data":{"channel":"live_trades"}}))

        return self.wst

    def send(self, msg):
        """
        Send message
        :param msg: Message
        :return:
        """
        self.ws.send(msg)

    def __start(self, reconnect_interval=10):
        while True:
            self.ws.run_forever()
            logger.info("Socket <%s> is going to reconnect..." % self.id)
            time.sleep(reconnect_interval)

    def __on_message(self, ws, m):
        if self._received_data_compressed is True:
            data = zlib.decompress(m, zlib.MAX_WBITS|16).decode('UTF-8')
            m = json.loads(data)
            print(m)
        else:
            m = json.loads(m)
            print(m)
        if len(self.on_message_handlers) > 0:
            for handler in self.on_message_handlers:
                handler(m)

    def __on_open(self, ws):
        logger.info("Socket <%s> is opened." % self.id)
        self._connected = True
        if len(self.on_open_handlers) > 0:
            for handler in self.on_open_handlers:
                handler(ws)
        
    def __on_close(self, ws):
        logger.info("Socket <%s> is closed." % self.id)
        self._connecting = False
        self._connected = False
        if len(self.on_close_handlers) > 0:
            for handler in self.on_close_handlers:
                handler(ws)
        
    def __on_error(self, ws, error):
        logger.info("Socket <%s> error:\n %s" % (self.id, error))
        if len(self.on_error_handlers) > 0:
            for handler in self.on_error_handlers:
                handler(ws, error)
