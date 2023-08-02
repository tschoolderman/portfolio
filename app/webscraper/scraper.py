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

    def get_tab_title(self):
        self.title = self.soup.select("title")[0].getText()

    def get_elements(self):
        if self.soup.select(".author"):
            for element in self.soup.select(".author"):
                self.result.append(element.text)

        elif self.soup.select(".title"):
            for element in self.soup.select(".title"):
                self.result.append(element.text)

        elif self.soup.select(".h6"):
            for element in self.soup.select(".h6"):
                self.result.append(element.text)

    def run(self, url):
        response = self.get_url(url)
        self.make_soup(response)
        self.get_tab_title()
        self.get_elements()


# if __name__ == "__main__":
#     scraper = Scraper()
#     scraper.run("https://dekudeals.com/")
