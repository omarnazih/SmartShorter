import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    SECRET_KEY = os.environ.get('SECRET_KEY')
        
    DB_NAME = 'SMARTSHORTNER'
    DB_USERNAME = 'ADMIN'
    DB_PASSWORD = os.environ.get('DB_PASSWORD')

    MONGO_URI = f'mongodb+srv://admin:{DB_PASSWORD}@cluster0.wffxo.mongodb.net/?retryWrites=true&w=majority'

    SESSION_COOKIE_SECURE = True    

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True 
    SESSION_COOKIE_SECURE = False       

class TestingConfig(Config):
    TESTING = True
    SESSION_COOKIE_SECURE = False       


