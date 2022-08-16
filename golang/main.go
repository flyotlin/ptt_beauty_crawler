package main

import (
	"fmt"
	"io"
	"net/http"
	"os"

	"github.com/gocolly/colly"
)

var idx = 1

func main() {
	c := colly.NewCollector()

	c.OnRequest(func(r *colly.Request) {
		r.Headers.Add("over18", "1")
	})
	baseUrl := "https://www.ptt.cc"
	url := fmt.Sprintf("%v/bbs/Beauty/index.html", baseUrl)
	c.Visit(url)

	c.OnHTML("div.r-ent div.title a", func(h *colly.HTMLElement) {
		href := h.Attr("href")
		fmt.Printf("Ele: %v - %v\n", h.Text, href)
		u := fmt.Sprintf("%v%v", baseUrl, href)
		c.Visit(u)
	})

	c.OnHTML("div.richcontent img", func(h *colly.HTMLElement) {
		src := h.Attr("src")
		fmt.Printf("Rich: %v\n", src)

		resp, err := http.Get(src)
		if err != nil {
			fmt.Printf("Error downloading image: %v\n", err.Error())
			return
		}
		defer resp.Body.Close()

		file, err := os.Create(fmt.Sprintf("dest/%v.jpg", idx))
		if err != nil {
			fmt.Printf("Error creating image: %v\n", err.Error())
			return
		}
		defer file.Close()

		_, err = io.Copy(file, resp.Body)
		if err != nil {
			fmt.Printf("Error copying image: %v\n", err.Error())
			return
		}
		idx += 1
	})

	over18Url := "https://www.ptt.cc/ask/over18"
	var data = map[string]string{
		"from": "/bbs/Beauty/index.html",
		"yes": "yes",
	}

	c.Post(over18Url, data)
}
