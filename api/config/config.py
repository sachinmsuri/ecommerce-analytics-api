import os
from decouple import config

BASE_DIR=os.path.dirname(os.path.realpath(__file__))

class Config:
    """
    Differnt Flask Configs depending if we are 
    developing, testing or deploying the application
    """

    #SECRET stored in .env
    SECRET_KEY=config('SECRET_KEY','secret')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevConfig(Config):
    """Config for Developement"""
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(BASE_DIR,'db.sqlite3')}"
    SQLALCHEMY_ECHO=True
    DEBUG=True

class TestConfig(Config):
    """Config for Testing"""
    TESTING=True
    SQLALCHEMY_DATABASE_URI=f"sqlite://"
    SQLALCHEMY_ECHO=True
    DEBUG=True

config_dict={
    'DEV':DevConfig,
    'TEST':TestConfig
}
