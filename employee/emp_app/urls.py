from django.urls import path
from .views import add_employee, get_employee_details

urlpatterns = [
    path('add-employee/', add_employee),
    path('get-employees/', get_employee_details),
]