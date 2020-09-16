from django.urls import path
from coffeeQuiz import views
urlpatterns = [
    path("", views.coffeeTasteQuiz, name="coffeeTasteQuiz")
]