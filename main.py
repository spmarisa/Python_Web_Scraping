import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import urllib.parse
import json
main_url = "http://www.hamleys.com"


def data_from_product_url(product_url):
    product_request = requests.get(product_url)
    product_content = BeautifulSoup(product_request.content, "lxml")

    info = product_content.find_all("img", {"class": "productMain"})
    name = info[0]['title']
    image_url = info[0]['src']
    image_name = image_url.split('/')[-1]
    urlretrieve(image_url, image_name)

    info = product_content.find_all("div", {"class": "productprice"})
    price = info[0].string

    info = product_content.find_all("div", {"class": "ftProductDescription"})
    description = info[0].contents[1]

    info = product_content.find_all("ul", {"class": "crumb blocklist"})
    blocks = info[0].find_all(href=True)
    tmp = []
    for block in blocks:
        tmp.append(block.string)
    categories = ' -> '.join(tmp)

    json_data = {}
    json_data['product_url'] = (product_url + "\n")
    json_data['name'] = (name + "\n")
    json_data['image_name'] = (image_name + "\n")
    json_data['image_url'] = (image_url + "\n")
    json_data['price'] = (price + "\n")
    json_data['description'] = (description + "\n")
    json_data['categories'] = (categories + "\n")

    with open('data.json', 'a') as outfile:
        json.dump(json_data, outfile)

def all_product_urls(category_url):
    category_request = requests.get(category_url)
    category_content = BeautifulSoup(category_request.content, "lxml")

    product_tags = category_content.find_all("li", {"class": "productThumbImage"})

    product_urls = []
    for product_url in product_tags:
        product_urls.append(main_url + "/" + product_url.product_url["href"])

    for product_url in product_urls:
        data_from_product_url(product_url)



main_request = requests.get(main_url)
main_content = BeautifulSoup(main_request.content, "lxml")

category_tags = main_content.find_all("ul", {"class": "topNav shopNav"})

category_names = category_tags[0].find_all("a", {"class": "menu"}, href=True)

category_urls = []

for category_name in category_names:
    category_urls.append(main_url + "/" + category_name["href"])

for category_url in category_urls:
    all_product_urls(category_url)
