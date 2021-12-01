from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<title>", views.entry, name="entry"),
    path('add', views.add, name = 'add'),
    path('edit/<title>', views.edit, name = "edit"),
    path('random', views.random, name = 'random'),
    path('find', views.find, name = "find")
]
