import urllib.request
import urllib3
from bs4 import BeautifulSoup

# url = "https://www.naver.com"
url = "https://news.naver.com/"
http = urllib3.PoolManager()
html = http.request("GET",url)
bs_obj = BeautifulSoup(html.data,"html.parser")
tag_lis = bs_obj.find("ul",{"class":"hdline_article_list"}).find_all("li")
lis = [li.find('div',{'class':'hdline_article_tit'}).find('a').text.strip() for li in tag_lis]
for li in lis:
    print(li)


#### urllib.resuest.urlopen Remote end closed connection without response Error 발생 - 버전 문제로 생각
#### urllib3로 변경하여 사용