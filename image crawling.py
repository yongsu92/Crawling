from selenium import webdriver


def search_selenium(search_name, search_path, search_limit):
    search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"

    browser = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
    browser.get(search_url)

    image_count = len(browser.find_elements_by_tag_name("img"))

    print("로드된 이미지 개수 : ", image_count)

    browser.implicitly_wait(2)

    for i in range(search_limit):
        image = browser.find_elements_by_tag_name("img")[i]
        image.screenshot("C:/Users/yskwo/Desktop/CrawlingImage/age_gender_estimation-master/image2/" + str(i) + ".jpg")

    browser.close()


if __name__ == "__main__":
    search_name = input("검색하고 싶은 키워드 : ")
    search_limit = int(input("원하는 이미지 수집 개수 : "))
    search_path = "Your Path"
    search_selenium(search_name, search_path, search_limit)