from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("htmlpage", views.htmlpage, name="htmlpage"),
    path("pythonpage", views.pythonpage, name="python-projects"),
    path("pygamepage", views.pygamepage, name="pygame-projects"),
    path("videospage", views.videospage, name="videos"),
    path("html_cheatsheet/<int:id>", views.html_cheatsheet, name="html_cheatsheet"),
    path("python_cheatsheet/<int:id>", views.python_cheatsheet, name="python_cheatsheet"),
    path("pygame_cheatsheet/<int:id>", views.pygame_cheatsheet, name="pygame_cheatsheet")
]