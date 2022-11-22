import requests
from bs4 import BeautifulSoup

baixa = requests.get("https://c.xkcd.com/random/comic/")
soup = BeautifulSoup(baixa.text, 'html.parser')
url_img = soup.select('div#comic img')[0]['src']
download_url = "https:{}".format(url_img)

print("baixando: {} ...".format(download_url))

with open('xkcd-scrapped.png', 'wb') as image: 
    image.write(requests.get(download_url).content)
