from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('generatedpassword/', views.password, name="password"),
    path('aboutus', views.aboutPage, name="aboutUs")
]
