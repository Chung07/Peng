#抓PTT國考版的HTML
import urllib.request as req
url="https://www.ptt.cc/bbs/Examination/index.html"
#建立一個request物件，附加Request Headers的資訊
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
})
#不要用網址，給request
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
# print(data)

#解析原始碼，取得每篇文的標題
#安裝第三方套件:pip install beautifulsoup4
import bs4
root=bs4.BeautifulSoup(data,"html.parser") #用html做解析
# print(root.title.string) #抓title標籤裡的文字

titles=root.find_all("div",class_="title") #尋找class="title" 的div標籤
# print(titles) #titles代表div .a找裡面的標籤a .strings取文字 被刪除的不會有a
for title in titles:
    if title.a !=None: #如果標題有a標籤就印出來
        print(title.a.string)

