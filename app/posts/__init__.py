from flask import Blueprint

bp = Blueprint("posts", __name__)

# does not work without this, eventhough it is unused
from app.posts import routes
