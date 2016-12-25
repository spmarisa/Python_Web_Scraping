import requests
from urllib.request import urlretrieve
import urllib.parse
from bs4 import BeautifulSoup
import json

url = "http://www.hamleys.com/nerf-nstrike-mega-mastodon-blaster.ir"
# url = "http://www.hamleys.com/hamleys-magic-drawing-board.ir"
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")

links = soup.find_all("img", {"class": "productMain"})
name = links[0]['title']
image = links[0]['src']

links = soup.find_all("div", {"class": "productprice"})
price = links[0].string

links = soup.find_all("div", {"class": "ftProductDescription"})
description = links[0].contents[1]

links = soup.find_all("ul", {"class": "crumb blocklist"})
# a = links[0].find_all("li")
a = links[0].find_all(href=True)
z = []
for b in a:
    z.append(b.string)
categories = ' -> '.join(z)

print(url)
print(name)
print(image)
print(price)
print(description)
print(categories)


image_url = image

file_name = image_url.split('/')[-1]

urlretrieve(image_url, file_name)



with open('data.json', 'a') as outfile:
    json.dump(r, outfile)
