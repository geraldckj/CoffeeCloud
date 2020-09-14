from django.urls import path
from . import views
urlpatterns = [
    # views.home is function in views
    # name is name of directory and corresponding function
    #name can be used to set url links
    path('home/', views.pub_homepage, name="coffeeCloud-pub_homepage"),
    path('', views.home, name="coffeeCloud-home"),
    path('about/', views.about, name="coffeeCloud-about"),
    path('log/', views.dailyLog, name="coffeeCloud-dailyLog"),
    path('addbean/', views.addBean, name="coffeeCloud-addBean"),
    path('contact/', views.contactForm, name="coffeeCloud-contactForm"),
    path('mybeans/', views.myBeans, name="coffeeCloud-myBeans"),
    path('logchoice/', views.logChoice, name="coffeeCloud-logChoice"),
    path('chiptest/', views.chipTest, name="coffeeCloud-chipTest"),
    path('chiptest2/', views.chipTest2, name="coffeeCloud-chipTest2"),
    path('mylog/', views.myLog, name="coffeeCloud-myLog"),
]
