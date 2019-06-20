from flask import Flask

from shengren.systests import injector_slot

app = Flask(__name__)

app.register_blueprint(injector_slot)

