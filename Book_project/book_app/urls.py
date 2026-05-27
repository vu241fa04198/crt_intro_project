from django.urls import path
from .views import add_book,home_page,contact_page,profile_page,portfolio_page,cont_page,grade_page,add_user

urlpatterns = [
    path('add/', add_book),
    path('home_page',home_page),
    path("contact_page",contact_page),
    path("profile_page",profile_page),
    path("portfolio_page",portfolio_page),
    path("cont_page",cont_page),
    path("<int:marks>",grade_page),
    path("user_form",add_user)


]