import requests
from bs4 import BeautifulSoup

ret = requests.get('https://www.python.org/')
text = ret.text
soup = BeautifulSoup(text, 'html.parser')
post_preview = soup.find_all('div', class_='medium-widget event-widget last')

for hub in post_preview:
    x = hub.find_all('li')
    for d in x:
        print(f'Дата проведения мероприятия: {d.find("time").text.strip()}')
        print(f'Название мероприятия: {d.find("a").text.strip()}')
        print(f'ССылка на мероприятие: https://www.python.org{d.find("a").get("href")}')
        print("----------------------------------------------------------------------------")

