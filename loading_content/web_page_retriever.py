import requests


class WebPageRetriever:

    def __init__(self, url):
        self.url = url
        self.response = None
        self.content = None

    def retrieve(self):
        self.response = requests.get(self.url)
        self.content = self.response.content




