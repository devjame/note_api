import os
from dotenv import load_dotenv


BASEDIR = os.path.dirname(__file__)
load_dotenv(os.path.join(BASEDIR, '.env'))
load_dotenv(os.path.join(BASEDIR, '.flaskenv'))


class Config:

    DATABASE_USER = os.getenv("DB_USER")
    DATABASE_PASSWORD = os.getenv("DB_PASSWORD")
    DATABASE_NAME = os.getenv("DB_NAME")
    DATABASE_IP = os.getenv("IP")
    DATABASE_PORT = os.getenv("PORT")

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_IP}:{DATABASE_PORT}/{DATABASE_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = b'\x90O\x1a\x88WA,;\xc6\xf4\xc3H\xdb\x91\x0bf'


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False


settings = {
    'development': DevConfig,
    'production': ProdConfig
}