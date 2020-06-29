
from flask import Flask
from config import Config
app = Flask(__name__)
wsgi_app = app.wsgi_app
app.config.from_object(Config)

from app import routes
#import config
