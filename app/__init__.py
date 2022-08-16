from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# Load Config File based on current ENV
INIT_CAP_ENV = app.config['ENV'].capitalize()
app.config.from_object(f"config.{INIT_CAP_ENV}Config")

print(f'Current ENV is [{INIT_CAP_ENV}]')

# Setup Mongodb
mongodb_client = MongoClient(app.config['MONGO_URI'])
db = mongodb_client.mydb


from app import routes