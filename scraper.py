import requests
from bs4 import BeautifulSoup

result = requests.get("https://google.com")

print(result.status_code)
print(result.headers)

src = result.content