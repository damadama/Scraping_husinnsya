from email import header
from urllib import response
import requests

response = requests.get("https://news.google.com/home?hl=ja&gl=JP&ceid=JP:ja")

# 
response.status_code

response.text

response.headers

# for key,value in response.headers.items():
#     print(key,"    ",value)

user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
header = {"user-agent": user_agent}
url="https://news.google.com/home?hl=ja&gl=JP&ceid=JP:ja"
response=requests.get(url,headers=header)
print(response.status_code)
param={"q":"python"}
response=requests.get("https://www.google.com/search",params=param)
print(response.text)




