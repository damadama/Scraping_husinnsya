from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
import chromedriver_binary
import datetime
from datetime import date
from datetime import timedelta
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import numpy as np
import csv
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException


# ヘッドレストの宣言
options=Options()
options.add_argument("--headless")


url="https://nordot.app/-/tags/%e7%a6%8f%e5%b2%a1%e7%9c%8c%e4%b8%8d%e5%af%a9%e8%80%85%e6%83%85%e5%a0%b1?unit=133089874031904245&all=true&ncmp=post_tag"

# optionでヘッドレストのオプションを追加
driver = webdriver.Chrome('chromedriver.exe',options=options) #chrome webdriverを起動、パスを指定
# driver = webdriver.Chrome('chromedriver.exe') #chrome webdriverを起動、パスを指定
driver.implicitly_wait(10)#chromeドライバーが見つかるまでの待ち時間を設定
driver.get(url) #URLにアクセス

#urlへ遷移する前に下の処理に行かないための記述
time.sleep(3)

# もっと見るボタンをクリックして情報を取る
x = 1

while True:
    try:
        #クリックの動作を入力
        #find_element_by_idはhtmlのidの要素を指定して入力できる
        # browser_from = driver.find_element(By.ID,'articleList_item--more')
        # browser_from = driver.find_element(By.CSS_SELECTOR,'articleList_moreIcon')
        # browser_from = driver.find_element({"method":"css selector","selector":".articleList_item--more"})
        # browser_from = driver.find_element({"method":"css selector","selector":"articleList_moreIcon"})
        browser_from = driver.find_element(By.XPATH,'//*[@id="js-btnViewMore"]')
        # browser_from = driver.find_element(By.CSS_SELECTOR,"#js-btnViewMore")
        # browser_from =driver.FindElement(By.CssSelector("input[value='登録']"))
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("window.scrollBy(0,-500);")
        browser_from.click()
        print('クリック：'+str(x))
        x = x + 1
        if x == 100:
            break
    except :
        time.sleep(3)
        alert = driver.switch_to_alert()
        alert.accept()
        print("Alert accepted")

# time.sleep(3600)

print("情報抜き出し")
time.sleep(3)
parse_html = BeautifulSoup(driver.page_source, 'html.parser')

elems=parse_html.find_all("h2",class_="articleList__title")
links=parse_html.find_all("a",class_="articleList__link")

j=0
titlelist=[]
for elem in elems:
    elem = elem.contents[0]
    titlelist.append(elem)
    # print(titlelist[j])
    j=j+1

j=0
link_list=[]
for link in links:
    link_list.append(link.get("href"))
    # print(link_list[j])
    j=j+1

# 一覧にまとめる
# news_list=zip(titlelist,link_list)
# print(list(news_list))

# リンク先に飛んで詳細情報を持ってくる
print("詳細リンク先に移動し、情報を取得")

j=0
syousai_list=[]
date_s_list=[]
base_url="https://nordot.app"
for link_s in link_list:
    url_s=base_url+str(link_s)
    r=requests.get(url_s)
    soup_s=BeautifulSoup(r.text, 'html.parser')
    syousai=soup_s.find("p",class_="ma__p").string
    date_s=soup_s.find("bdi").string
    syousai_list.append(syousai)
    date_s_list.append(date_s)
    # print(syousai_list[j])
    # print(date_s_list[j])
    j=j+1


# titlelistから発生場所と犯罪の分類を分ける
address_list=[]
classification_list=[]

for test in titlelist:
    # 住所の抜き出し
    target="で"
    idx=test.find(target)
    r=test[:idx]

    target2="）"
    idx=r.find(target2)
    r2=r[idx+1:]
    address="福岡県"+r2.replace("付近","")
    # print(address)

    # 犯罪分類抜き出し
    target="　"
    idx=test.find(target)
    r=test[:idx]

    target2="で"
    idx=r.find(target2)
    r2=r[idx+1:]
    classification=r2
    # print(classification)
    
    address_list.append(address)
    classification_list.append(classification)

# 情報を一つのリストにまとめる
news_list=np.stack([classification_list,address_list,date_s_list, syousai_list], 1)

# csvファイルに書き込み
with open("data.csv","w") as file:
    writer = csv.writer(file,lineterminator="\n")
    writer.writerows(news_list)


#少し待機する
time.sleep(3)
#インスタンスウインドウのみ閉じる
driver.close()
print("終了しました")
# print(titlelist)
