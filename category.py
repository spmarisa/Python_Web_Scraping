import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import urllib.parse
import json
main_url = "http://www.hamleys.com"


def all_product_urls(category_url):
    category_request = requests.get(category_url)
    category_content = BeautifulSoup(category_request.content, "lxml")

    product_tags = category_content.find_all("li", {"class": "productThumbImage"})
    product_urls = []

    for product_url in product_tags:
        product_urls.append(main_url + "/" + product_url.a["href"])

    return product_urls

all_product_urls("http://www.hamleys.com/preschool-baby.irc")
