import imp
from django.urls import path

from .views import home, about

app_name = "pages"
urlpatterns = [
    path('', home, name="home"),
    path("about/", about, name="about")
]
