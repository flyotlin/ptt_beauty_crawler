import requests
from bs4 import BeautifulSoup
import os

class Url:
    __url = ""
    __htmlSource = ""
    __soup = ""
    __aTags = ""
    __link = []
    def __init__(self, url):
        # super().__init__()
        self.url = url

    def get_url(self):
        return self.__url

    def get_link(self):
        return self.__link

    def get_htmlSource(self):
        return self.__htmlSource
    
    def get_soup(self):
        return self.__soup

    def set_htmlSource(self, res):
        self.__htmlSource = res

    def set_soup(self, soup):
        self.__soup = BeautifulSoup(soup.text, "html.parser")

    def set_aTags(self, selector):
        self.__aTags = self.__soup.select(selector)

    def set_link(self):
        for i in self.__aTags:
            i = "https://www.ptt.cc/" + i['href']
            self.__link.append(i)

def fetch(url):
    res = requests.get(url, cookies={'over18': '1'})
    return res

def get_htmlSource(res):
    Url.set_htmlSource(Url, res)

def soup(html):
    Url.set_soup(Url, html)

def soup_select(selector):
    Url.set_aTags(Url, selector)

# used for downloading, need to pass the html
def download(file_name, html):
    with open(file_name, "wb") as file:
        file.write(html.content)
        file.flush()
    file.close()


