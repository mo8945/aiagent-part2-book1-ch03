import requests

url = "https://hn.algolia.com/api/v1/search"
params = {
    "query": "AI",
    "tags": "story"
}

response = requests.get(url, params=params)

data = response.json()
articles = data["hits"]

for article in articles:
    title = article.get("title")
    created_at = article.get("created_at")
    print(title, created_at)