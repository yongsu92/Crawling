from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
import urllib
import time
import sys,re,os,math,random

f_dir = "C:/Users/yskwo/Desktop/CrawlingImage/age_gender_estimation-master/image2/"

path = 'C:\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(path)
s_time = time.time()

search_name = input('검색하고 싶은 키워드를 입력하세요 : ')
search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"
driver.get(search_url)
time.sleep(2)

def scroll_down(driver):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(1)
scroll_down(driver)

file_no = 0
count = 1
img_src2 = []

html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
img_src = soup.find('div',{"class":"islrc"}).find_all('img')
print(img_src[0])
for i in img_src:
    try:
        img_src1 = i['src']
    except:
        img_src1 = i['data-src']
    else:
        img_src2.append(img_src1)
        count += 1

for i in range(0,len(img_src2)):
    try:
        urllib.request.urlretrieve(img_src2[i],f_dir+str(file_no)+'.jpg')
    except:
        continue
    file_no += 1
    time.sleep(0.5)
    print(f'{file_no}번째 이미지를 저장중 입니다=============================')
e_time = time.time()
t_time = e_time-s_time
print('='*70)
print(f'총 소요시간은 {t_time}초 입니다.')
driver.close()
