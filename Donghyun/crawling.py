# crawling.py
# use Python3 to perform website crawling
# help from http://hleecaster.com/python-web-crawling-with-beautifulsoup/

import requests
from bs4 import BeautifulSoup
import re

if __name__ == "__main__":
    web = requests.get("https://www.daangn.com/hot_articles")
    soup = BeautifulSoup(web.content, "html.parser")

    soup.find_all(re.compile("[ou]l"))
    soup.find_all(re.compile("h[1-9]"))
    soup.find_all(['h1', 'p'])
    soup.find_all(attrs={'class': 'card-title'})
    soup.find_all(attrs={'class': 'footer-list', 'id': 'footer-address-list'})
