"""day_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from app02 import views

"""
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^home/', views.home.as_view()),
    #url(r'^detail/', views.detail),
    url(r'^detail-(\d+).html', views.detail),
    url(r'^detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail),

]
"""

urlpatterns = [
    url(r'^cmdb/', include("app02.urls")),
    url(r'^monitor/', include("app03.urls")),
    url(r'^business/',views.business),
    url(r'^host/',views.host)

]

