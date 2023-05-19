
from django.urls import path

from schools import views

urlpatterns = [
    path("add", views.add),
    path("list/", views.list),
]
