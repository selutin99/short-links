import os


class BaseConfig:
    CORS_ENABLED = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or '9OLWxND4o83j4K4iuopO'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Database config
    POSTGRES_URL = os.environ.get('POSTGRES_URL') or "127.0.0.1:5432"
    POSTGRES_USER = os.environ.get('POSTGRES_USER') or "postgres"
    POSTGRES_PW = os.environ.get('POSTGRES_PW') or "postgres"
    POSTGRES_DB = os.environ.get('POSTGRES_DB') or "short_links"

    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER, pw=POSTGRES_PW,
                                                                   url=POSTGRES_URL, db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = DB_URL


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    CORS_ENABLED = True


class ProductionConfig(BaseConfig):
    DEBUG = False
