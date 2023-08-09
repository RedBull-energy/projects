from django.urls import path
from django.urls import path, include
from . import views
from users.views import get_success_url

urlpatterns = [
    path('', views.chatPage, name="chat-page"),
    path("home/", get_success_url, name="home"),

]
