from django.urls import path

from notification import views

app_name = 'notification'

urlpatterns = [
    path('my_notification/', views.my_notification, name='my_notifications'),
    path('my_responses/', views.my_responses, name='my_responses'),
    path('my_match/', views.my_match, name='my_match'),
]
