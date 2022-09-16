from django.urls import path

from sigapp import views

urlpatterns = [
    path('register/', views.Student_profile, name='register'),
]