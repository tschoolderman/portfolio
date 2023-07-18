from flask import Blueprint

bp = Blueprint("webscraper", __name__)

from app.webscraper import routes
