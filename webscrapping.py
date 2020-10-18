import requests
from bs4 import BeautifulSoup
result = requests.get("https://www.dan.me.uk/tornodes/")
#print(result.status_code)
#print(result.headers)
src = result.content
#print (src)
soup = BeautifulSoup(src, 'lxml')
print(soup)
links = soup.find_all('__BEGIN_TOR_NODE_LIST__')
print(links)
#print("\n")
