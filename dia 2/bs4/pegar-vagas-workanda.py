import requests
from bs4 import BeautifulSoup

url = 'https://www.workana.com/jobs?category=it-programming&language=pt&subcategory=web-development'
user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64)"
baixar = requests.get(url, headers={ 'User-Agent': user_agent })
soup = BeautifulSoup(baixar.text, 'html.parser')

vagas = soup.find_all('h2', class_="h3 project-title")

url_base = 'https://www.workana.com'
novas_vagas = []

for vaga in vagas:
    novas_vagas.append({
            "titulo": vaga.findChild('a').findChild('span').text,
            "url": url_base + vaga.findChild('a')['href']
            })

print(novas_vagas)
