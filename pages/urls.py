from django.urls import path
from . import views

urlpatterns = [
    path("", views.about_view, name="about"),
    path("contact/", views.contact_view, name="contact"),
]