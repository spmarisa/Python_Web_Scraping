import requests
from bs4 import BeautifulSoup

url = "http://www.hamleys.com"
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")

links = soup.find_all("ul", {"class": "topNav shopNav"})


z = links[0].find_all("a", {"class": "menu"})

for i in z:
    print(i)
