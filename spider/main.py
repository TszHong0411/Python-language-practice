import requests
from bs4 import BeautifulSoup
import json 

url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=ssd&page=1&sort=sale/dc"
res = requests.get(url)
data = json.loads(res.text)

allProducts = data["prods"]

for product in allProducts:
    print(product["name"])
    print(product["price"])
    print("\n")
