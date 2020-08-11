from django.utils.timezone import now


class SharedContent:
    USER_REF = None


def fine_social_user(user_name):
    print("Searching for user name " + user_name)
    from app.models import SocialUserSearch
    from app.core.modules.sherlock.sherlock import search_username

    try:
        content = SocialUserSearch.objects.get(username=user_name)
        print(content.username, content.search_status)
        SharedContent.USER_REF = content
        try:
            search_username(user_name)
        except:
            print("Failed to perform some operations")
        SocialUserSearch.objects.filter(id=content.id).update(finished_at=now(), search_status=True)

    except Exception as e:
        print('Failed at start execution ' + str(e))
