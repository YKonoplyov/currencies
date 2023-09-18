import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = os.getenv("POSTGRES_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'


develop = DevelopmentConfig()

testing = TestingConfig()