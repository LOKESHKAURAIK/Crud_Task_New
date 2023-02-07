from django.urls import path
from . import views
urlpatterns = [
    path("", views.home),
    path("addstudent", views.addstudent),
    path("search", views.search),
    path("delete", views.delete),
    path("delete_pro", views.delete_pro),
    path("update", views.update),
    path("update_pro", views.update_pro),


]
