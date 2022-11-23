from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('register/', views.registerPage, name='registerPage'),
    path('login/', views.loginPage, name='loginPage'),
]
