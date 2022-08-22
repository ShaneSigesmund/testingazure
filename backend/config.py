
import os


class Config(object):
    """Default configuration"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(16)


class ProductionConfig(Config):
    """Production environment configuration"""
    DEBUG = False
    PERMANENT_SESSION_LIFETIME = 7200
    SUPPRESS_WARNINGS = True

    #SQL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://sales_admin@salesapp:CatRabbitDog@123@salesapp.mysql.database.azure.com/sales_tool'

config = Config