import crawler as cl
import requests
from bs4 import BeautifulSoup

page_count = 21
attemp_url__ff = "" + str(page_count)

directory_path = "./photo/"


cl.check_path(directory_path)

def main(page_url, page_count):
    count = 1
    page = cl.Crawl(page_url)
    page.link = []
    page.parse_aTags("div.thread-item a")
    page.set_link("", "")
    for i in page.link:
        if(i == "https://www.pttweb.cc/bbs/Gossiping"):
            continue
        post = cl.Crawl(i)
        post.link = []
        post.parse_aTags("a.externalHref")
        post.set_link("", "")
        print(post.link)
        for t in post.link:
            if ("i.imgur.com" not in t):
                continue
            if (".gif" in  t):
                continue
            file_path = directory_path + "Page" + str(page_count) +  " Photo" + str(count) + ".jpg"
            count += 1
            # hplink = cl.Crawl(t)
            # no new instantiate makes the process faster
            hplink = requests.get(t)
            post.download(file_path, hplink)
        print("==========================")

while(page_count <= 61):
    main(attemp_url__ff, page_count)
    page_count += 1
    attemp_url__ff = "" + str(page_count)
    print("=============NEXT PAGE!!!!!!!=============")