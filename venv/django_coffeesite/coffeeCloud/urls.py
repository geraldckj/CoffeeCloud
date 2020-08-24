from django.urls import path
from . import views
urlpatterns = [
    # views.home is function in views
    # name is name of directory and corresponding function
    #name can be used to set url links
    path('', views.pub_homepage, name="coffeeCloud-pub_homepage"),
    path('home/', views.home, name="coffeeCloud-home"),
    path('about/', views.about, name="coffeeCloud-about"),
]
