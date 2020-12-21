import requests
from bs4 import BeautifulSoup

url = "https://www.eosgo.io/"

result = requests.get(url=url)
print(result)
bs_obj = BeautifulSoup(result.content,"html.parser")
h3 = bs_obj.find_all("h3",{"class":"title"})
print(h3)