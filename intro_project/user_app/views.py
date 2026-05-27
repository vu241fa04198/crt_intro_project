from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def greet(request):
    return HttpResponse("Hii, Good Morning")


def get_name(request):
    return HttpResponse("Hii, yamuna")


def user_data(request):
    data = [
        {
            "name": "rajitha",
            "email": "rajitha@gmail.com",
            "address": "hyd"
        },
        {
            "name": "jaya",
            "email": "jaya@gmail.com",
            "address": "hyd"
        },
        {
            "name": "ammulu",
            "email": "ammu@gmail.com",
            "address": "hyd"
        }
    ]

    return JsonResponse(data, safe=False)