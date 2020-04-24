import requests
from bs4 import BeautifulSoup
import os
import time

# check whether the object directory exists
def check_path(path):
    if(os.path.exists(path) == False):
        os.mkdir(path)

class Crawl:
    url = ""
    html = ""
    soup = ""
    aTags = ""
    link = []
    
    # init, constructor
    def __init__(self, url):
        self.url = url
        self.fetch_html()
        self.parse_soup()
    
    # request the html source
    def fetch_html(self):
        self.html = requests.get(self.url, cookies={'over18': '1'})
    
    def parse_soup(self):
        self.soup = BeautifulSoup(self.html.text, "html.parser")
    
    def parse_aTags(self, selector):
        self.aTags = self.soup.select(selector)

    def set_link(self, http, jpg):
        for t in self.aTags:
            t = http + t['href'] + jpg
            self.link.append(t)

    # download the jpg as binary
    def download(self, file_path, html):
        with open(file_path, "wb") as file:
            file.write(html.content)
            file.flush()
        file.close()



