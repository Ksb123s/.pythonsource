from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from urllib.request import urlretrieve

def set_chrome_driver():
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def main():
    browser = set_chrome_driver()

    browser.get("https://www.naver.net")


    element = browser.find_element(By.ID, "query")
    print(element)

    # 검색어 입력 + 엔터
    element.send_keys("아이스크림")
    element.send_keys(Keys.ENTER)
    # browser.quit()

    time.sleep(2)

    imgClick = browser.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[1]/a')

    imgClick.click()
    time.sleep(2)
    interval = 3

    # 현재 문서 높이를 가져와서 저장
    prev_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        time.sleep(interval)

        cur_height = browser.execute_script("return document.body.scrollHeight")

        if cur_height == prev_height:

            break

        prev_height = cur_height

    browser.execute_script("window.scrollTo(0, 0)") 
    time.sleep(interval)
    
    count =1
    iceImages = browser.find_elements(By.CSS_SELECTOR, ".thumb img")    
    for iceImage in iceImages:
        try:
            iceImage.click()
            time.sleep(interval)
            # 큰이미지
            # //*[@id="main_pack"]/section[1]/div/div/div[1]/div[2]/div[1]/img
            #  div.viewer_image img 

            img_url = browser.find_element(By.CSS_SELECTOR, "div.viewer_image img").get_attribute("src")
            # print(img_url)
            # urlretrieve("다운로드 받을 파일 경로", "저장경로")
            urlretrieve(img_url, "C:\\source\\pythonsource\\crawl\\download\\"+str(count)+".jpg")
            count+=1
        except:
            pass


    time.sleep(2)

if __name__ == "__main__":
        main()