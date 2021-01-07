



import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    web = requests.get("https://www.daangn.com/hot_articles")
    soupsource = BeautifulSoup(web.content, "html.parser")

    print(soupsource.find_all("h1"))