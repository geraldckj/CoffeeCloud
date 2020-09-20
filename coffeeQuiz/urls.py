from django.urls import path
from coffeeQuiz import views
urlpatterns = [
    path("", views.coffeeTasteQuiz, name="coffeeQuiz-coffeeTasteQuiz"),
    path("reccomendations/", views.reccomendations, name="coffeeQuiz-reccomendedBeans")
]