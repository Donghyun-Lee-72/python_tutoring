##crawling.py

import requests
from bs4 import BeautifulSoup

   def get_html(url):
      _html = ""
      resp = requests.get(url)
      if resp.status_code == 200:
         _html = resp.text
      return _html

if __name__ == "__main__":
    pass
