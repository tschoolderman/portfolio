from dynaconf import Dynaconf
from sqlalchemy.engine import URL


class Config:
    settings = Dynaconf(
        environments=True,
        settings_files=["settings.toml", ".secrets.toml"],
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
