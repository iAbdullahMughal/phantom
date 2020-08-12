import requests
from bs4 import BeautifulSoup
from django.utils.timezone import now
import lxml.html
from app.core.modules.search_engine.google_search import google_search


class SharedContent:
    USER_REF = None


def fine_social_user(user_name):
    print("Searching for user name " + user_name)
    from app.models import SocialUserSearch
    users = SocialUserSearch.objects.all()
    for user in users:
        print(user.username, str(user.search_status))
    from app.core.modules.sherlock.sherlock import search_username

    try:
        content = SocialUserSearch.objects.get(username=user_name)
        print(content.username, str(content.search_status))
        SharedContent.USER_REF = content
        try:
            search_username(user_name)
        except:
            print("Failed to perform some operations")

        SocialUserSearch.objects.filter(id=content.id).update(finished_at=now(), search_status=True)

    except Exception as e:
        print('Failed at start execution ' + str(e))

    search_on_google(query=user_name)


def search_on_google(query):
    from app.models import GoogleSearchModel
    print("Starting Search on Google")
    links = google_search(query)
    for link in links:
        hearders = {'headers': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'}
        n = requests.get(link, headers=hearders)
        soup = BeautifulSoup(n.text, features="lxml")
        title = soup.find('title')
        # print(title.get_text())

        GoogleSearchModel.objects.create(
            username=SharedContent.USER_REF,
            site_title=title.get_text(),
            google_link=link
        )
