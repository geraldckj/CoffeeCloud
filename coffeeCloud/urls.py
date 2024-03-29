from django.urls import path
from . import views
urlpatterns = [
    # views.home is function in views
    # name is name of directory and corresponding function
    #name can be used to set url links
    path('', views.home, name="coffeeCloud-home"),
    path('about/', views.about, name="coffeeCloud-about"),
    path('log/', views.dailyLog, name="coffeeCloud-dailyLog"),
    path('addBean/', views.addBean, name="coffeeCloud-addBean"),
    path('contact/', views.contactForm, name="coffeeCloud-contactForm"),
    # path('feedback/', views.feedback, name='coffeeCloud-feedback'),
    path('mybeans/', views.myBeans, name="coffeeCloud-myBeans"),
    path('logchoice/', views.logChoice, name="coffeeCloud-logChoice"),
    path('mylog/', views.myLog, name="coffeeCloud-myLog"),
]
