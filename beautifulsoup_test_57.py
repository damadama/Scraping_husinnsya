import requests
from bs4 import BeautifulSoup

url="https://www.yomiuri.co.jp/"
# url="https://nordot.app/-/tags/%e7%a6%8f%e5%b2%a1%e7%9c%8c%e4%b8%8d%e5%af%a9%e8%80%85%e6%83%85%e5%a0%b1?unit=133089874031904245&all=true&ncmp=post_tag"

res=requests.get(url)

# textの内容を確認
# print(res.text)

# パーサー（解析機）で解析にかける
soup=BeautifulSoup(res.text,"html.parser")

# 解析ツールで選択⇒copy selectで取得
elems=soup.select("div.headline > article:nth-child(1) > div > h3 > a")

# タイトルの取得
print(elems[0].contents[0])
# リンクの取得
print(elems[0].attrs["href"])


# 複数のニュースタイトルを取得
elems = soup.select("div.headline")
# 内容の確認
# print(elems[0].prettify)

print(elems[0].h3.a.string)
# print(elems[0].h3.a["href"])
print(elems[0].div.wrap.next_siblings)
