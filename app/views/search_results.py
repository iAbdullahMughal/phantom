import json

from django.http import HttpResponse

from app.models import SocialUserSearch
from phantom.celery import start_execution


def check_username(username):
    try:
        content = SocialUserSearch.objects.get(username=username)
        print(content.id)
        return True, content.id
    except:
        return False, None


def create_username(username):
    try:
        content = SocialUserSearch.objects.create(
            username=username,
            search_status=False
        )
        return True, content.id
    except:
        return False, None


def searched_usernames(request):
    content = {
        'has_error': True,
        'error_message': None,
    }
    user_name = request.POST.get('user_name', '')
    if not user_name:
        content['has_error'] = True
        content['error_message'] = {
            'title': 'Username required!',
            'description': 'Please enter username before search.'
        }
        content = json.dumps(content)
        return HttpResponse(content, content_type="application/json")

    else:
        status_code, user_id = check_username(user_name)
        print(user_id)
        if status_code:
            found = {'has_error': False, 'id':user_id}
            found = json.dumps(found)
            return HttpResponse(found, content_type="application/json")
        else:
            status_code, user_id = create_username(user_name)
            if status_code:
                print("Calling Service for searching user")
                start_execution.delay(user_name)
                new_user_id = {'has_error': False, 'id': user_id}

                new_user_id = json.dumps(new_user_id)
                return HttpResponse(new_user_id, content_type="application/json")
