from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Book
from .models import UserMode

@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        book_data = Book.objects.create(
            book_id=data.get("book_id"),
            name=data.get("name"),
            price=data.get("price"),
            author=data.get("author"),
            publish_date=data.get("publish_date"),
            title=data.get("title"),
            category=data.get("category"),
        )

        return JsonResponse({
            "book_id": book_data.book_id,
            "message": "Book added successfully",
        })

    return JsonResponse({"error": "Only POST method allowed"})

from django.shortcuts import render
#create your views here
def home_page(request):
    return render(request, "home.html")

def home_page(request):
    return render(request, "home.html")
def contact_page(request):
    return render(request, "contact.html")
def profile_page(request):
    return render(request, "profile.html", {
        "name": "Amit",
        "email": "amit@gmail.com",
        "role": "admin",
        "user_data": [
            {"name": "Amit", "email": "amit@gmail.com"},
            {"name": "Geetha", "email": "geetha@gmail.com"},
            {"name": "Kajal", "email": "kajalgmail.com"},
            {"name":"pooja","email":"pooja@gmail.com"}
        ]
    })





def portfolio_page(request):
    return render(request, "portfolio.html")
def cont_page(request):
    return render(request, "cont.html")
def grade_page(request,marks):
    return render(request, "grade.html",{"marks":marks})

def add_user(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        data=UserMode.objects.create(
            name=name,
            email=email,

        )
        return HttpResponse("User added successfully")
    return render(request,"user_form.html")