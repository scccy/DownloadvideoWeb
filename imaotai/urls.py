from django.urls import path

from . import views

urlpatterns = [
    path("mobile", views.get_mobile, name="mobile"),
    path("location", views.get_loaction, name="location"),
    # path("settings/", views.settings, name="tksettings"),
]
