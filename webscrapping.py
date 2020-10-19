import requests
from bs4 import BeautifulSoup


def get_ips():
    result = requests.get("https://www.dan.me.uk/torlist/")
    src = result.content

    soup = BeautifulSoup(src, "lxml")

    ip = soup.p.text
    return ip

