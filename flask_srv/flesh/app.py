from flask import Flask

from shengren.systests.flask import inject

app = Flask(__name__)

app.register_blueprint(inject)

