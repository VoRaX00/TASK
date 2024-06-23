from django.urls import path

from homework import views

app_name = 'homework'

urlpatterns = [
    path('', views.view_homework, name='view_homework'),
]