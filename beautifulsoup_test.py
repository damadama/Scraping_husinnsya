
from bs4 import BeautifulSoup

# html="https://news.yahoo.co.jp/"

html = """
<html>
    <head>
        <title>清水義孝の著書</title>
    </head>
    <body>
        <p class="title">
            <b>清水義孝の最新の著書には、次の本があります。</b>
        </p>
        <p class="recent books">
            <a class="book" href="https://www.amazon.co.jp/dp/B07TN4D3HG" id="link1">Python3によるビジネスに役立つデータ分析入門</a>、
            <a class="book" href="http://www.amazon.co.jp/dp/B07SRLRS4M" id="link2">よくわかるPython3入門2.NumPy・Matplotlib編</a>、
            <a class="book" href="http://www.amazon.co.jp/dp/B07T9SZ96B" id="link3">よくわかるPython3入門4.Pandasでデータ分析編</a>
        </p>
        <p class="end">
            <b>そして、これらの本は好評発売中です。</b>
        </p>
    </body>
</html>
"""

soup=BeautifulSoup(html,"html.parser")

# 文字の取得
# print(soup.body.p.next_sibling.next_sibling.a.string)
# リンクの取得
# print(soup.body.p.next_sibling.next_sibling.a["href"])

# for文を回してテキストを順番に取ってくる
# for tag_a in soup.find_all("a"):
#     print(tag_a.string)
#     print(tag_a["href"])




