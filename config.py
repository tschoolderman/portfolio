from dynaconf import Dynaconf
from sqlalchemy.engine import URL


class Config:
    settings = Dynaconf(
        environments=True,
        settings_files=[".secrets.toml"],
    )

    SQLALCHEMY_DATABASE_URI = URL.create(
        "mysql+pymysql",
        username=settings.DB_USERNAME,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME,
    )

    SQL_ALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = settings.MAIL_SERVER
    MAIL_PORT = settings.MAIL_PORT
    MAIL_USERNAME = settings.MAIL_USERNAME
    MAIL_PASSWORD = settings.MAIL_PASSWORD
    MAIL_USE_TLS = settings.MAIL_USE_TLS
    MAIL_USE_SSL = settings.MAIL_USE_SSL
