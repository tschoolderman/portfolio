from flask import render_template

from app.webscraper import bp
from app.webscraper.scraper import Scraper


@bp.route("/")
def index():
    scraper = Scraper()
    scraper.run()
    return render_template(
        "webscraper/index.html",
        title=scraper.title,
        results=scraper.result,
    )
