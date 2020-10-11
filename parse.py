import requests
from bs4 import BeautifulSoup

URL = 'https://www.sulpak.kz/f/smartfoniy/almaty/'

HEADERS ={'accept':'*/*', 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
HOST = 'https://www.sulpak.kz'

def get_html(url,params=None):
    r = requests.get(url,headers=HEADERS,params=params)
    return r

def get_conternt(html):
    soup = BeautifulSoup(html, 'html.parser')
    product = soup.find_all('a', class_='tile-container')

    phone = []
    for product in product:
        phone.append({
            'title':product.find('a', class_='title').get_text(),
            'price':product.find('div', class_="price").get_text(),
        })
    print(phone)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        phone = get_content(html.text)
    else:
        print('Error')

parse()
