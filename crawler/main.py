import crawler as cl

def main():
    # initial variable
    attempt = "https://www.ptt.cc/bbs/Beauty/index.html"
    directory_path = "./photo/"
    count = 1

    cl.check_path(directory_path)

    # instantiate
    page = cl.Crawl(attempt)
    page.parse_aTags("div.title a")
    page.set_link("https://www.ptt.cc", "")

    # 考慮如果下載耗時甚久的話
    for t in page.link:
        post = cl.Crawl(t)
        # don't know why we need to clear link every time, isn't it instantiated every time
        post.link = [] 
        post.parse_aTags("a")
        post.set_link("", "")
        for i in post.link:
            if(i[2] == "i") & (i[3] == "m"):
                print(i)
                file_path = directory_path + "Photo" + str(count) + ".jpg"
                count += 1
                i = "http:" + i + ".jpg"
                hplink = cl.Crawl(i)
                post.download(file_path, hplink.html
        print("==========================")

    
main()