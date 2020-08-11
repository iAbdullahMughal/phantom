import requests
from bs4 import BeautifulSoup

from app.core.helper.get_proxy import GetProxy

proxies = GetProxy.gen_proxy()
print(proxies)
payload = {'username': 'Mahdoom2011', 'target':'all4webs'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36'
                  ' (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get('https://knowem.com/usercheckv2.php?target=all4webs&username=Mahdoom2011', headers=headers,
                         data=payload)

print(response.content)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup)