from django.urls import path

from . import views

urlpatterns = [
    path("search/", views.search, name="tkSearch"),
    path("download/", views.download_video, name="tkdownload"),
    path("account/", views.account, name="tkaccount"),
    path("text/", views.text, name="text"),
    # path("settings/", views.settings, name="tksettings"),
]