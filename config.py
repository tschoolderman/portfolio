from os import path

from dynaconf import Dynaconf

basedir = path.abspath(path.dirname(__file__))


class Config:
    settings = Dynaconf(
        environments=True,
        settings_files=[".secrets.toml"],
    )

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(basedir, "portfolio.db")

    SQL_ALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = settings.MAIL_SERVER
    MAIL_PORT = settings.MAIL_PORT
    MAIL_USERNAME = settings.MAIL_USERNAME
    MAIL_PASSWORD = settings.MAIL_PASSWORD
    MAIL_USE_TLS = settings.MAIL_USE_TLS
    MAIL_USE_SSL = settings.MAIL_USE_SSL
