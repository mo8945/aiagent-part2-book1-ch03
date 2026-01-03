from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import requests
import os

# 1. headless 옵션
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

# 2. 페이지 열기
url = "https://news.naver.com/section/105"
driver.get(url)
time.sleep(3)

# 3. 기사 카드 기준 선택 (상위 영역)
articles = driver.find_elements(By.CSS_SELECTOR, "li.sa_item")[:10]

os.makedirs("news_images", exist_ok=True)

results = []

for idx, article in enumerate(articles, start=1):
    # 제목
    title = article.find_element(By.CSS_SELECTOR, "strong.sa_text_strong").text

    # 이미지
    img = article.find_element(By.CSS_SELECTOR, "img")
    img_url = img.get_attribute("src")

    # 이미지 저장
    img_res = requests.get(img_url)
    file_name = f"news_images/news_{idx}.jpg"
    with open(file_name, "wb") as f:
        f.write(img_res.content)

    results.append((idx, title, file_name))
    print(f"{idx}. {title} → {file_name}")

driver.quit()
