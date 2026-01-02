import requests
import pandas as pd

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
print(df.head())