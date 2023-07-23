from flask import Flask

from app.extensions import db, mail
from app.main import bp as main_bp
from app.posts import bp as posts_bp
from app.questions import bp as questions_bp
from app.webscraper import bp as webscraper_bp
from config import Config


# Factory function
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config.from_prefixed_env()

    # Initialize Flask extensions here
    db.init_app(app)
    mail.init_app(app)

    # Register blueprints here
    app.register_blueprint(main_bp)
    app.register_blueprint(posts_bp, url_prefix="/posts")
    app.register_blueprint(questions_bp, url_prefix="/questions")
    app.register_blueprint(webscraper_bp, url_prefix="/webscraper")

    @app.route("/test/")
    def test_page():
        return "<h1>Testing the Flask Application Factory Pattern</h1>"

    return app
