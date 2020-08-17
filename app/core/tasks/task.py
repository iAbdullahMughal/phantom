import requests
from bs4 import BeautifulSoup
from django.utils.timezone import now
import lxml.html

from app.core.modules.instantusername.instant_username_search import InstantUsernameSearch
from app.core.modules.search_engine.google_search import google_search


class SharedContent:
    USER_REF = None


def fine_social_user(user_name):
    print("Searching for user name " + user_name)
    from app.models import SocialUserSearch
    from app.core.modules.sherlock.sherlock import search_username
    user_id = None
    try:
        content = SocialUserSearch.objects.get(username=user_name)
        print(content.username, str(content.search_status))
        SharedContent.USER_REF = content
        try:

            search_username(user_name)
        except:
            print("Failed to perform some operations")
    except Exception as e:
        print('Failed at start execution ' + str(e))
    #
    try:
        search_on_google(query=user_name)
    except:
        print("Failed to fetch results from google")

    search_on_instant(user_name, SharedContent.USER_REF)

    SocialUserSearch.objects.filter(id=SharedContent.USER_REF.id).update(finished_at=now(), search_status=True)


def search_on_instant(username, ref):
    try:
        obj = InstantUsernameSearch()
        obj.add_record(username, ref)
    except:
        print("Failed to get results from Instant User names")


def search_on_google(query):
    from app.models import GoogleSearchModel
    print("Starting Search on Google")
    try:
        links = google_search(query)
        for link in links:
            hearders = {'headers': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'}
            n = requests.get(link, headers=hearders)
            soup = BeautifulSoup(n.text, features="lxml")
            title = soup.find('title')
            try:
                print(title.get_text())
                GoogleSearchModel.objects.create(
                    username=SharedContent.USER_REF,
                    site_title=title.get_text(),
                    google_link=link
                )
            except Exception as e:
                print("Failed to search results from google. " + str(e))
    except:
        print("Failed to get user results from google.")
