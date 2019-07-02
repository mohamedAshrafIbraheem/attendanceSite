# Use include() to add paths from the catalog application
from django.urls import include
from django.urls import path

from students import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginView, name='login'),
    path('register/',views.RegisterView, name='register'),
]