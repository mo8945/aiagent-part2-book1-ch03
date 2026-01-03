import requests
from bs4 import BeautifulSoup

url = "https://m.news.naver.com/section/105"
headers = {"User-Agent": "Mozilla/5.0"}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

imgs = soup.select("img[data-src*='mimgnews.pstatic.net']")
print("이미지 수:", len(imgs))
print(imgs[0]["src"] if imgs else "없음")

# <img class="_LAZY_LOADING _LAZY_LOADING_INIT_HIDE" width="110" height="75" alt="" style="" src="https://mimgnews.pstatic.net/image/origin/031/2026/01/02/993812.jpg?type=nf220_150">