from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



desired_caps = {
    "platformName": "Android",
    "appium:deviceName": "Samsung Galaxy S7 edge",
    "browserName": "chrome",  
    "appium:platformVersion": "8",
    "appium:automationName": "UIAutomator2",
}

# Appium 서버에 연결

count_num = 0
for forTest in range(1,6):
  
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    try:
            # 웹 페이지로 이동
            driver.get('https://kakaopayinscorp.co.kr/products/FAA001')
            current_url = driver.current_url
            print(f"현재 1페이지의 URL: {current_url}")

    # 웹 페이지 로딩 대기
            time.sleep(2)
     
     # 버튼이 있는 좌표 설정 (원하는 좌표로 수정)
            x_coord = 455
            y_coord = 1760
    
            TouchAction(driver).tap(x=x_coord, y=y_coord).perform()
            current_url = driver.current_url
            print(f"현재 2페이지의 URL: {current_url}")
    
            last_url = 'https://talk.kakaoinsure.com/bridge/corp/products?productCode=FAA001&dc=DIR100&utm_source=kpins_website&utm_medium=b2c_faa001&utm_campaign=website_faa001_pd_pdcta_20231114&utm_content=nov4'
            if(current_url == last_url):
                {
                    print("TestPass")
                }

            else:
                {
                     print("TestPail")
                }

            count_num = count_num + 1
            print(f"현재 테스트횟수 : {count_num}")
            time.sleep(2)

    finally:
            if(count_num == 5):
                {
                print(f"최종테스트횟수 : {count_num}"):
                #print(f"현재 테스트횟수 : {count_num}")
                # 세션 종료
                driver.quit()
                }
