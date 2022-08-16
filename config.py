import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    SECRET_KEY = os.environ.get('SECRET_KEY')        
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    DB_NAME = 'mydb'
    DB_USERNAME = 'admin'
    DB_PASSWORD = os.environ.get('DB_PASSWORD')

    if not DB_PASSWORD:
        DB_PASSWORD = '42F7iDLNt002Xagy'

    MONGO_URI = f'mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@cluster0.wffxo.mongodb.net/{DB_NAME}?retryWrites=true&w=majority'
        
    SESSION_COOKIE_SECURE = True    

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True 
    SESSION_COOKIE_SECURE = False       

class TestingConfig(Config):
    TESTING = True
    SESSION_COOKIE_SECURE = False       


