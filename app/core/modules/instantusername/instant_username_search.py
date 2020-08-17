import json

import requests


class InstantUsernameSearch:
    SITES = []
    END_POINT = "https://api.instantusername.com/check/"

    def __init__(self):
        git_url = "https://raw.githubusercontent.com/instant-username-search/instant-username-search-api/" \
                  "master/src/main/resources/static/sites.json"
        response = requests.get(url=git_url)
        try:
            content = json.loads(response.text)

            for site in content:
                if site not in self.SITES:
                    self.SITES.append(site)
        except Exception as e:
            print(e)

    def add_record(self, user_name, user_ref):
        from app.models import InstantUsernameModel
        print("Going to search records on instant user name")
        for site in self.SITES:
            response = requests.get(self.END_POINT + site + "/" + user_name)

            try:
                print(response.text)
                content =  response.json()
                print("instant username search : " + content["service"] + " --- " + content["url"])
                if not content["available"]:
                    InstantUsernameModel.objects.create(
                        username=user_ref,
                        website_name=content["service"],
                        website_url=content["url"],
                    )
            except Exception as e:
                print("Failed to create record in Instant Search table " + str(e))
