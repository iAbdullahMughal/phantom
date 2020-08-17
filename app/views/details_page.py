from django.shortcuts import render
from app.models import SocialUserSearch, SocialUserFound, GoogleSearchModel, InstantUsernameModel


def check_user_id(user_id):
    try:
        content = SocialUserSearch.objects.get(id=user_id)
        return True, content
    except:
        return False, None


def get_user_names(user_id):
    try:
        s_object = SocialUserSearch.objects.get(id=user_id)
        try:
            details = SocialUserFound.objects.filter(username=s_object.id)
            usernames = []
            for detail in details:
                usernames.append(
                    {
                        'website_name': detail.website_name,
                        'website_url': detail.website_url,
                    }
                )
            return True, usernames
        except Exception as e:
            print(e)
            return False, None

    except Exception as e:
        print(e)
        return False, None


def google_records(user_id):
    try:
        s_object = SocialUserSearch.objects.get(id=user_id)
        try:
            details = GoogleSearchModel.objects.filter(username=s_object)
            links = []
            for link in details:
                links.append(
                    {
                        'link': link.google_link,
                        'title': link.site_title
                    }
                )
            return True, links
        except:
            return False, None
    except:
        return False, None

def get_instant_user_records(user_id):

    try:
        details = InstantUsernameModel.objects.filter(username=user_id)
        links = []
        for detail in details:
            links.append(
                {
                    'website_name': detail.website_name,
                    'website_url': detail.website_url,
                }
            )
        return True, links
    except Exception as e:
        print(e)
        return False, None

def search_completed(user_id):
    s_object = SocialUserSearch.objects.get(id=user_id)
    return s_object.search_status


def user_details(request):
    content = {
        "has_found": False,
        "error_message": "",
        "is_running": False,
        "details": {

        }
    }
    try:
        user_id = request.GET.get('user_id', '')
        status_code, username_info = check_user_id(user_id)
        if not status_code:
            content["has_found"] = True
            content["error_message"] = "Please enter/select correct user id, to check the details."
        else:
            content["search_id"] = username_info.id
            content["username"] = username_info.username
            if search_completed(user_id):
                print("Fetching data")
                status_code, usernames = get_user_names(user_id)
                content["details"] = {
                    'usernames': usernames
                }
                status_code, google_links = google_records(user_id)
                content["google_links"] = google_links

                status_code, username_links = get_instant_user_records(user_id)
                content["instantusername"] = username_links
            else:
                content["is_running"] = True

    except Exception as e:
        content["has_found"] = True
        content[
            "error_message"] = "Failed to perform action against request. Please try again with correct information."

    return render(request, 'pages/details.html', {'content': content})
