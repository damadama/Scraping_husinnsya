
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

# ヘッドレストの宣言
options=Options()
options.add_argument("--headless")

# optionでヘッドレストのオプションを追加
driver = webdriver.Chrome(r"C:\Users\windu\Documents\chromedriver_win32\chromedriver",options=options) 

driver.get("https://www.google.com/")

search_bar=driver.find_elements_by_name("q")
search_bar[0].send_keys("python")

search_bar[0].submit()

for elem_h3 in driver.find_elements_by_xpath("//a/h3"):
    print(elem_h3.text)
    elem_a=elem_h3.find_element_by_xpath("..")
    print(elem_a.get_attribute("href"))
    







