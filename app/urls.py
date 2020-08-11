from django.conf.urls import url

from app.views.home_page import RecentSocialRunList
from app.views.search_results import searched_usernames

urlpatterns = [
    # url('phone_number_added', phone_number_added, name="phone_number_added"),
    url('username', searched_usernames, name="search_username"),
    url('recent_user_search', RecentSocialRunList.as_view(), name="recent_user_search"),
]
