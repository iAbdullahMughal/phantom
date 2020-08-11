"""phantom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static

from app.views.details_page import user_details
from app.views.home_page import home_page
from phantom import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    url('^user_details/$', user_details, name='user_details'),
    re_path('search/', include('app.urls')),

]
