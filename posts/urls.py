from django.urls import path
from posts import views


urlpatterns = [
    path("", views.home_view),
]
