import requests
from bs4 import BeautifulSoup

url = "http://www.hamleys.com/"
r = requests.get(url)

# r.content



# soup = BeautifulSoup(r.content)
soup = BeautifulSoup(r.content, "html")

# print(soup.prettify())

links = soup.find_all("a")
#
# for link in soup.find_all("a"):
#     print(link)
#
# for link in soup.find_all("a"):
#     link.get("href")
#
# for link in soup.find_all("a"):
#     print(link.get("href"))
#
# for link in soup.find_all("a"):
#     print(link.text)

for link in links:
    if "http" in link.get("href"):
        "<a href='%s'>%s</a>" %(link.get("href"), link.text)


g_data = soup.find_all("a", {"class": "business-name"})
print(g_data)

for item in g_data:
    print(item.text)

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import requests
from bs4 import BeautifulSoup

url = "http://www.hamleys.com/"
r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")


links = soup.find_all("a href='%s' class='menu'>'%s'</a>")

    "a href='%s' class="menu">'%s'</a>"
    <a href="preschool-baby.irc" class="menu">Baby</a>

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

with open('data.json', 'a') as outfile:
    json.dump(r, outfile)
