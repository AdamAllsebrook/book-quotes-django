from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add-quote/", views.add_quote, name="add_quote"),
]
