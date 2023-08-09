from django.urls import path
from . import views
from .views import activate
app_name = 'home'
urlpatterns = [

    path('', views.login_view, name="login"),
    path("signup/", views.signup, name="signup"),
    path("home/", views.get_success_url, name="home"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
    activate, name='activate'),

]
