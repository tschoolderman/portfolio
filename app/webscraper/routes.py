from flask import render_template, request

from app.models.webscraperform import WebscraperForm
from app.webscraper import bp
from app.webscraper.scraper import Scraper


@bp.route("/", methods=["GET", "POST"])
def index():
    scraper = Scraper()
    webscraper = WebscraperForm()

    if request.method == "POST":
        input_url = "https://" + webscraper.url.data
        scraper.run(input_url)
        return render_template(
            "webscraper/index.html",
            title=scraper.title,
            results=scraper.result,
            form=webscraper,
        )
    else:
        scraper.run("https://quotes.toscrape.com/")
        return render_template(
            "webscraper/index.html",
            title=scraper.title,
            results=scraper.result,
            form=webscraper,
        )
