from django.urls import path
from . import views

urlpatterns = {
    path("hello/", views.hello, name="hello"),
    path("welcome/", views.welcome, name="welcome"),
    path("intro/", views.intro, name="intro"),
    path("name/", views.name, name="name"),

}
