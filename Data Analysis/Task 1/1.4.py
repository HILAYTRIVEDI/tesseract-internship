import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for item in data[:]:
        print(f"Title: {item['title']}\nBody: {item['body']}\n")
else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")
