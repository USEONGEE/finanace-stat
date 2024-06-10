from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def crowling_data(id):
    # ChromeDriver 설정
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    try:
        # 지정된 URL로 이동
        url = f"https://place.map.kakao.com/{id}"
        driver.get(url)

        # 페이지가 로드될 시간을 기다림 (필요에 따라 조정)
        time.sleep(2)
        # num_rate 클래스를 가진 모든 요소 찾기
        rates = driver.find_elements(By.CSS_SELECTOR, ".num_rate")

        if rates:
            # 마지막 요소 선택
            last_element = rates[-2]
            print(last_element)

            # 마지막 요소의 텍스트 가져오기
            text = last_element.text
            print(text)
        else:
            print("No elements found with the class 'num_rate'")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()


crowling_data(8403570)
