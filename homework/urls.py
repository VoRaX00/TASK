from django.urls import path

from homework import views

app_name = 'homework'

urlpatterns = [
    path('view_homework/', views.view_homework, name='view_homework'),
    path('add_homework/', views.add_homework, name='add_homework'),
]
