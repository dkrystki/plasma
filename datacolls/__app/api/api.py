import threading

from ptcomm.systests import injector_slot
from flask import Flask
import flask_restful


class Api(object):
    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.app.register_blueprint(injector_slot)

        self.api = flask_restful.Api(self.app)

        self.thread = threading.Thread(target=self.worker)

    def worker(self) -> None:
        self.app.run(host='0.0.0.0', port=80, use_reloader=False, debug=True)

    def start(self) -> None:
        self.thread.start()
