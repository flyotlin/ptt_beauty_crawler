import requests
from bs4 import BeautifulSoup
import os

def check_path(path):
    if(os.path.exists(path) == False):
        os.mkdir(path)

def fetch(url):
    response = requests.get(url)
    response = requests.get(url, cookies={'over18': '1'})
    return response


folder_path = "./photo/second/"
check_path(folder_path)

# the page to crawl
url = "https://www.ptt.cc/bbs/Beauty/index3276.html"
content = fetch(url)

soup = BeautifulSoup(content.text, "html.parser")
a_tags = soup.select('div.title a')
link = []   # each article's link
for t in a_tags:
    t = "https://www.ptt.cc/" + t['href']
    link.append(t)

## go into each page
count = 1
for i in link:
    url = i
    content = fetch(url)
    soup = BeautifulSoup(content.text, "html.parser")
    src = soup.select("a")

    for j in src:
        # differentiate "imgur"
        if (j['href'][2] == "i") & (j['href'][3] == "m"):
            j = "https:" + j['href'] + ".jpg"
            content = requests.get(j)   ## the html content of url j
            file_name = folder_path + "photo" + str(count) + ".jpg"
            count += 1
            with open(file_name, "wb") as file:
                file.write(content.content)
                file.flush()
            file.close()

