from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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

        # 특정 버튼을 찾고 클릭 (CSS Selector 사용)
        while True:
            try:
                # #mArticle > div.cont_evaluation > div.evaluation_review > a > span.txt_more
                button_selector = "#mArticle > div.cont_evaluation > div.evaluation_review > a > span.txt_more"
                button = driver.find_element(By.CSS_SELECTOR, button_selector)
                button.click()
                time.sleep(0.05)
            except:
                break

        # 특정 li 태그 하위의 모든 자식을 크롤링 (CSS Selector 사용)
        li_selector = "#mArticle > div.cont_evaluation > div.evaluation_review > ul"
        ul_element = driver.find_element(By.CSS_SELECTOR, li_selector)

        li_selector = "li"
        li_elements = ul_element.find_elements(By.CSS_SELECTOR, li_selector)

        result = []
        for li in li_elements:
            try:
                # #mArticle > div.cont_evaluation > div.evaluation_review > ul > li:nth-child(2) > div.comment_info > p > span
                data_selector = "div.comment_info > p > span"
                data_element = li.find_element(By.CSS_SELECTOR, data_selector)
                result.append(data_element.text)
            except:
                pass

    finally:
        # 브라우저 닫기
        driver.quit()
        return result
