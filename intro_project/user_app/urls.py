from django.urls import path, include
from .views import greet,get_name,user_data
#http://127.0.0.1:8000/message
#http://127.0.0.1:8000/name

urlpatterns = [
    path('message', greet),
    path('name', get_name),
    path('data', user_data)
]
