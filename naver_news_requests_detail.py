import requests
from bs4 import BeautifulSoup
import os
import time

BASE_URL = "https://news.naver.com"
SECTION_URL = "https://news.naver.com/section/105"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

os.makedirs("news_images", exist_ok=True)

# =========================
# 1. 섹션 페이지 요청
# =========================
res = requests.get(SECTION_URL, headers=HEADERS)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

articles = soup.select("li.sa_item")[:10]

print(f"기사 수집 시작 ({len(articles)}개)\n")

# =========================
# 2. 기사 상세페이지 처리
# =========================
for idx, article in enumerate(articles, start=1):
    title = article.select_one("strong.sa_text_strong").get_text(strip=True)
    link = article.select_one("a.sa_text_title")["href"]

    print(f"{idx}. {title}")

    # -------------------------
    # 상세 페이지 요청
    # -------------------------
    detail_res = requests.get(link, headers=HEADERS)
    detail_res.raise_for_status()

    detail_soup = BeautifulSoup(detail_res.text, "html.parser")

    # -------------------------
    # 본문 이미지 추출
    # -------------------------
    
    img_url = None

    # 1️⃣ og:image (대표 이미지)
    meta_img = detail_soup.select_one("meta[property='og:image']")
    if meta_img and meta_img.get("content"):
        img_url = meta_img["content"]

    # 2️⃣ 본문 이미지 (fallback)
    if not img_url:
        body_img = detail_soup.select_one("div#newsct_article img")
        if body_img and body_img.get("src"):
            img_url = body_img["src"]

    if img_url:
        img_data = requests.get(img_url, headers=HEADERS).content
        file_path = f"news_images/news_{idx}.jpg"
        with open(file_path, "wb") as f:
            f.write(img_data)
        print(f"   이미지 저장: {file_path}")
    else:
        print("   이미지 없음")

print("\n크롤링 완료")