import crawler as cl

# initial variable
attempt = "https://www.ptt.cc/bbs/Beauty/index3278.html"
directory_path = "./photo/"
count = 1

cl.check_path(directory_path)
# instantiate
page = cl.Crawl(attempt)
page.parse_aTags("div.title a")
page.set_link("https://www.ptt.cc", "")


# 考慮如果下載耗時甚久的話
for t in page.link:
    # print(t)
    post = cl.Crawl(t)
    post.parse_aTags("a")
    post.set_link("", "")
    for i in post.link:
        # print(i)
        if(i[2] == "i") & (i[3] == "m"):
            file_path = directory_path + "Photo" + str(count) + ".jpg"
            count += 1
            i = "http:" + i + ".jpg"
            hplink = cl.Crawl(i)
            post.download(file_path, hplink.html)
    
