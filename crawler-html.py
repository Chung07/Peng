from requests_html import HTMLSession

session=HTMLSession()
r=session.get("https://www.ptt.cc/bbs/Examination/index.html")
#獲取頁面html
print(r.html.html)