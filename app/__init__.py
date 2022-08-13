from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

# Loading Configs from config file
app.config.from_object('config.DevelopmentConfig')

# Setup Mongodb
mongodb_client = PyMongo(app)
db = mongodb_client.db


from app import routes