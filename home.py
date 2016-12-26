import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import urllib.parse
import json
main_url = "http://www.hamleys.com"

main_request = requests.get(main_url)
main_content = BeautifulSoup(main_request.content, "lxml")

category_tags = main_content.find_all("ul", {"class": "topNav shopNav"})

category_names = category_tags[0].find_all("a", {"class": "menu"}, href=True)

category_urls = []

for category_name in category_names:
    category_urls.append(main_url + "/" + category_name["href"])
