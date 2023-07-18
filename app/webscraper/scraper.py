import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self) -> None:
        self.result = []
        self.title = ""
        self.soup = None

    def get_url(self, url):
        return requests.get(url)

    def make_soup(self, html):
        self.soup = BeautifulSoup(html.text, "lxml")

    def get_title(self):
        self.title = self.soup.select("title")[0].getText()

    def get_authors(self):
        for author in self.soup.select(".author"):
            self.result.append(author.text)

    def run(self):
        response = self.get_url("https://quotes.toscrape.com/")
        self.make_soup(response)
        self.get_title()
        self.get_authors()


# if __name__ == "__main__":
#     scraper = Scraper()
#     scraper.run()
