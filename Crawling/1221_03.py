import requests
from bs4 import BeautifulSoup

url = "https://www.oliveyoung.co.kr/store/display/getMCategoryList.do?dispCatNo=1000001000100010001&fltDispCatNo=&prdSort=01&pageIdx=1&rowsPerPage=24&searchTypeSort=btn_thumb&plusButtonFlag=N&isLoginCnt=0&aShowCnt=0&bShowCnt=0&cShowCnt=0&trackingCd=Drawer_Cat100000100010001_Cat"
result = requests.get(url)
print(result)
bs_obj = BeautifulSoup(result.content,'html.parser')
print(bs_obj)