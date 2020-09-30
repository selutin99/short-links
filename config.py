import os


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '9OLWxND4o83j4K4iuopO'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Database config
    POSTGRES_URL = "127.0.0.1:5432"
    POSTGRES_USER = "postgres"
    POSTGRES_PW = "75297529S"
    POSTGRES_DB = "short_links"

    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER, pw=POSTGRES_PW,
                                                                   url=POSTGRES_URL, db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = DB_URL


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
