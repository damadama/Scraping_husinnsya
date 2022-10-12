import requests
from bs4 import BeautifulSoup
import re

url="https://nordot.app/-/tags/%e7%a6%8f%e5%b2%a1%e7%9c%8c%e4%b8%8d%e5%af%a9%e8%80%85%e6%83%85%e5%a0%b1?unit=133089874031904245&all=true&ncmp=post_tag"

res=requests.get(url)

# textの内容を確認
# print(res.text)

# パーサー（解析機）で解析にかける
soup=BeautifulSoup(res.text,"html.parser")

elems=soup.select("li:nth-child(1) > a > div.articleList__titleWrapper > h2")
print(elems[0].contents[0])

elems_s=soup.select("li:nth-child(1) > a > div.articleList__titleWrapper > p")
print(elems_s[0].contents[0])

elems_link=soup.select("#post > li:nth-child(1) > a")
print(elems_link[0].attrs["href"])

elems_link=soup.select("#post")
print(elems_link[0].li.a["href"])


elems=soup.find_all("h2",class_="articleList__title")

titlelist=[]
for elem in elems:
    elem = elem.contents[0]
    titlelist.append(elem)

print(titlelist)