from django.conf.urls import url

from app.views.search_results import searched_usernames

urlpatterns = [
    # url('phone_number_added', phone_number_added, name="phone_number_added"),
    url('username', searched_usernames, name="search_username"),
]
