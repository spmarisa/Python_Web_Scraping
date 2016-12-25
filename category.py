import requests
from bs4 import BeautifulSoup

url = "http://www.hamleys.com/arts-crafts.irc"
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")

links = soup.find_all("li", {"class": "productThumbImage"})

for a in links:
    a.a["href"]


links
