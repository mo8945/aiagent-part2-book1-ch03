import requests
from bs4 import BeautifulSoup
import os

url = "https://news.naver.com/section/105"

headers = {
    "User-Agent":"Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

imgs = soup.select("li.sa_item img[src*='mimgnews.pstatic.net']")

print(len(imgs))
os.makedirs("images", exist_ok=True)

for i, img in enumerate(imgs, start=1):
    img_url = img["src"]
    img_res = requests.get(img_url, headers=headers)
    
    file_name = f"images/new_{i}.jpg"
    
    with open(file_name, "wb") as f:
        f.write(img_res.content)
    
    print(f"{file_name} 저장완료")
    
    #_SECTION_HEADLINE_LIST_9ho0t > li:nth-child(2) > div > div > div.sa_thumb._LAZY_LOADING_ERROR_HIDE > div > a > img