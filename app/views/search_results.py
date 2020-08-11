import json

from django.http import HttpResponse

from app.core.modules.sherlock.sherlock import sherlock, search_username


def searched_usernames(request):
    content = {
        'has_error': True,
        'error_message': None,
    }
    user_name = request.POST.get('user_name', '')
    print(user_name)
    if not user_name:
        content['has_error'] = True
        content['error_message'] = {
            'title': 'Username required!',
            'description': 'Please enter username before search.'
        }
        content = json.dumps(content)
        return HttpResponse(content, content_type="application/json")
    else:
        site_results = search_username(user_name)
        content['has_error'] = False
        content['has_found'] = True
        content['site_results'] = site_results
    
        content = json.dumps(content)
        return HttpResponse(content, content_type="application/json")
