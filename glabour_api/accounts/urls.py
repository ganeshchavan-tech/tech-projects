from .views import registerView
from django.urls import path, include


urlpatterns = [
    path('register/',registerView.as_view()),
]