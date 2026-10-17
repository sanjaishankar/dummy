from django.urls import path
from . import views

urlpatterns = [
    path("people/", views.create_person, name="create_person"),
]