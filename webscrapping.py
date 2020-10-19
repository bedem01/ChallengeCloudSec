import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.dan.me.uk/torlist/")

src = result.content

soup = BeautifulSoup(src, "lxml")

print(soup.p.text)

