import requests
import pandas as pd
from datetime import datetime


url = "https://hn.algolia.com/api/v1/search"
params = {
    "query": "AI",
    "tags": "story"
}

response = requests.get(url, params=params)

data = response.json()
articles = data["hits"]

structured_data = []

for article in articles:
    structured_data.append({
        "title": article.get("title"),
        "author": article.get("author"),
        "date": article.get("title"),
        "url": article.get("url")
    })
    
df = pd.DataFrame(structured_data)
# print(df.head())

df["collected_at"] = datetime.now()
# print(df.head())

df.to_csv("news_daily.csv", index=False, encoding="utf-8-sig")
# print("데이터 수집 및 저장 완료")

today = datetime.now().strftime("%Y-%m-%d")
df.to_csv(f"news_{today}.csv", index=False, encoding="utf-8-sig")
# print("데이터 수집 및 저장 완료")