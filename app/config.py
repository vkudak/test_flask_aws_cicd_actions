import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    # SQLALCHEMY_DATABASE_URI = (os.environ.get('SQLALCHEMY_DATABASE_URI')
    #                            or 'sqlite:///' + os.path.abspath("app/database/database.db"))

    # SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') if os.getenv(
    #     'SQLALCHEMY_DATABASE_URI') else 'sqlite:///' + os.path.abspath("app/database/database.db")
