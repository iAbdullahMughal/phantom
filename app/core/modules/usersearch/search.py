import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0', 'X-Requested-With': 'XMLHttpRequest',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}


def search_one(username):
    url = "https://usersearch.org/results_normal.php"
    param = {
        "ran": "",
        "username": str(username)
    }
    response = requests.post(url=url, params=param, headers=headers)
    print(response.text)
def pwned(email):
    url = "https://usersearch.org/results_pwned.php"
    param = {
        "ran": "",
        "username": str(email)
    }
    response = requests.post(url=url, params=param, headers=headers)
    print(response.text)


def search_two(username):
    r = requests.get('https://usersearch.org/results_advanced.php?URL_username=' + str(username), headers=headers)
    soup = BeautifulSoup(r.text, features="lxml")
    mydivs = soup.findAll("div", {"class": "results-item"})
    for div in mydivs:
        found_on = div.findAll("p")[0].get_text()
        link = div.findAll("a")[0]
        web_link = link["href"]
        image = div.findAll("img")[0]
        image_link = image["src"]
        print(found_on, web_link, image_link)

def search_three(username):
    r = requests.get('https://usersearch.org/results_advanced1.php?URL_username=' + str(username), headers=headers)
    soup = BeautifulSoup(r.text, features="lxml")
    mydivs = soup.findAll("div", {"class": "results-item"})
    for div in mydivs:
        found_on = div.findAll("p")[0].get_text()
        link = div.findAll("a")[0]
        web_link = link["href"]
        image = div.findAll("img")[0]
        image_link = image["src"]
        print(found_on, web_link, image_link)

def search_four(username):
    r = requests.get('https://usersearch.org/results_advanced2.php?URL_username=' + str(username), headers=headers)
    soup = BeautifulSoup(r.text, features="lxml")
    mydivs = soup.findAll("div", {"class": "results-item"})
    for div in mydivs:
        found_on = div.findAll("p")[0].get_text()
        link = div.findAll("a")[0]
        web_link = link["href"]
        image = div.findAll("img")[0]
        image_link = image["src"]
        print(found_on, web_link, image_link)

pwned('iabdullahmughal@gmail.com')
# search_three('iabdullahmughal')
# search_four('iabdullahmughal')
#
#
#
# soup = BeautifulSoup(r.text, features="lxml")
#
# # soup.find
# mydivs = soup.findAll("div", {"class": "results-item"})
# for div in mydivs:
#     found_on = div.findAll("p")[0].get_text()
#     link = div.findAll("a")[0]
#     web_link = link["href"]
#     image = div.findAll("img")[0]
#     image_link = image["src"]
#     print(found_on, web_link, image_link)
#     # print(div)
