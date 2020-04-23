import crawler as cl

attempt = "https://www.ptt.cc/bbs/Beauty/index.html"
# instantiate
page = cl.Url(attempt)
res = cl.fetch(page.get_url)
cl.get_htmlSource(res)
cl.soup(page.get_htmlSource)
cl.soup_select("div.title a")
page.set_link()

for i in page.get_link:
    post = cl.Url(i)
