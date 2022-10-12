
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r"C:\Users\windu\Documents\chromedriver_win32\chromedriver") 

driver.get("https://www.google.com/")

search_bar=driver.find_elements_by_name("q")
search_bar[0].send_keys("python")

search_bar[0].submit()

i=0
while True:
    i=i+1
    sleep(1)
    for elem_h3 in driver.find_elements_by_xpath("//a/h3"):
        print(elem_h3.text)
        elem_a=elem_h3.find_element_by_xpath("..")
        print(elem_a.get_attribute("href"))
    next_link=driver.find_element_by_id("pnnext")
    driver.get(next_link.get_attribute("href"))
    if i > 4:
        break







