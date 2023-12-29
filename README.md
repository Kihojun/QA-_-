# QA-_-
#QA엔지니어 사전과제 제출용#

##프로젝트 이름##: **테스트 자동화 플랜과 테스트 코드**

###프로젝트 설명####
카카오페이손해보험의 해외여행보험 프로젝트 중 해외여행 보험 상품 진입 방법에 대한 테스트 케이스 중 자동화 영역에 대한 플랜 입니다.

##1.테스트 프레임워크 선정 기준##
----------------------------------------------------------------
**1. 프로젝트 요구사항:**
   1-1 카카오페이손해보험의 해외여행 보험 테스트 대상 범위 기준
   모바일 애플리케이션 범위가 많아 Appium 자동화도구 선정
   1-2 작성 언어
   테스트 코드를 작성할 수 있는 언어의 지원 여부를 고려
   사용성이 높은 파이썬 언어를 선정

##2.GUI로 자동화 가능한 영역##
--------------------------------------------------------------
* UI 자동화 도구: AutoIt, SikuliX, WinAppDriver 등을 사용하여
  간단한 진입 경로에 대한 반복 테스트를 목적으로 자동화 영역 설정*

*1.테스트 목적*
  - 카카오손해보험 온보딩 페이지 진입 후 [내 보험료 알아보기] 버튼 동작에 대한 반복 테스트

*2.확인 사항*
  - 버튼을 통한 페이지 이동 확인
  - 네트워크 오류로 인한 오류 페이지 이동
  - 버튼 무반응 현상 체크

*3. 테스트 코드 관련*
  - 카카오손해보험 페이지와 [내 보험료 알아보기] 버튼 동작 후
    페이지 비교를 통한 결과 비교를 목적으로 작성 하였습니다.     
-----------------------------------------------------------------
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

count_num = 0
for forTest in range(1,6):
    # Appium 서버에 연결
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
-----------------------------------------------------------
*3.API 자동화 가능한 영역*
-----------------------------------------------------------
작성한 테스트 기준으로 예상 가능한 자동화 영역 선정
**1.테스트 케이스 선정 이유**
금액 별 조정 문구에 따른 가이드 문구 변경 확인을 목적으로 
테스트 케이스 대상으로 선정하였습니다.

**2.테스트 케이스 예시**
(테스트스텝)
1.[내 보험료 알아보기] 선택
2.여행가는 나라 선택 완료
3.출발일/도착일 선택 완료
4.[다음] 선택
5.원하시는 보장을 선택해주세요 화면
6.많은 분들이 조정한 보장이에요 영역 
7.물건을 도둑맞았거나 부서졌을때 영역 
8.금액 조정 0단계 설정
(기대결과)
1.하기와 같은 구성으로 노출 확인
물건을 도둑맞았거나 부서졌을때
40만원
미가입 ㅣ   ㅣ  ㅣ100만원
세번째로 많이 선택한 보장이에요
(테스트스텝)
1.[내 보험료 알아보기] 선택
2.여행가는 나라 선택 완료
3.출발일/도착일 선택 완료
4.[다음] 선택
5.원하시는 보장을 선택해주세요 화면
6.많은 분들이 조정한 보장이에요 영역 
7.물건을 도둑맞았거나 부서졌을때 영역 
8.금액 조정 1단계 설정
(기대결과)
1.하기와 같은 구성으로 노출 확인

물건을 도둑맞았거나 부서졌을때
60만원
미가입 ㅣ   ㅣ  ㅣ100만원
60만원의 보장을 가장많이 선택했어요

*예시*
import requests

def get_guide(amount):
    api_url = 'https://example.com/api/guide'
    
    # 요청에 사용될 데이터
    data = {
        'amount': amount
    }

    # API 호출
    response = requests.get(api_url, params=data)

    # 응답 결과 확인
    if response.status_code == 200:
        guide_text = response.json().get('guide_text')
        print(f"Guide for amount {amount}: {guide_text}")
    else:
        print(f"Failed to get guide. Status Code: {response.status_code}, Response: {response.text}")

#금액에 따른 가이드 문구를 테스트

get_guide(100)

get_guide(500)

get_guide(1000)

*4.자동화 구현 중 발생 할 수 있는 문제점 및 해결 방안*
---------------------------------------------------
*1. UI 요소의 변동성 (UI Element Locators Change)*
문제현상 : 웹 또는 데스크톱 애플리케이션의 UI 요소들의 식별자가 자주 변경되면, 기존의 자동화 스크립트는 실패할 수 있습니다.
해결방안 : UI가 변경되면 해당 변경을 반영하여 테스트 코드를 유지보수하고 리팩터링하는 습관을 가집니다. 주기적으로 테스트 코드를 검토하고 수정합니다

*2.환경 의존성 (Environment Dependency)*
문제현상: 자동화 스크립트가 환경에 의존적일 경우 (예: 특정 브라우저, 특정 운영체제), 다른 환경에서 실행할 때 문제가 발생할 수 있습니다.
해결방안: 지속적인 환경 구성 및 테스트 실행에 대한 고려가 필요합니다.

*3.테스트 유지 보수*
문제현상: 애플리케이션의 변경으로 인해 테스트가 유효하지 않아질 수 있습니다.
해결방안: 정기적인 코드 리뷰 및 유지 보수, 테스트 케이스를 유지하기 쉬운 방식으로 작성한다

*4.지연된 응답과 타이밍 이슈 (Delayed Response and Timing Issues)*
문제현상: 서버 응답이 예상보다 느릴 경우, 타이밍 문제로 인해 테스트가 실패할 수 있습니다.
해결방안: 대기 시간 사용, 재시도 메커니즘 구현, 네트워크 속도 및 부하 고려하여 작성한다.

*5.테스트 리포트 구성 방안*
---------------------------------------------------------
*1.리포트 도구 선택*
팀 내 협의를 통해 테스트 리포트를 생성하고 표시하는 도구를 선택합니다 

*2.테스트 수행 결과 포함*
각 테스트 케이스의 실행 결과를 포함하여, 테스트가 성공했는지 실패했는지, 또는 중단된 경우에 대한 정보를 작성

*3.실패한 테스트의 원인 포함*
실패한 이유를 명확하게 기록하고, 필요한 경우 스크린샷을 첨부하여 디버깅 및 문제 해결에 도움을 줄수있습니다.

*4.커버리지 정보 포함 및 테스트 환경 정보 포함*
테스트가 실행된 환경에 대한 정보 및 기능 커버리지 정보를 표시하여 테스트 커버리지 공유
