from django.urls import path
from django.contrib import admin
from . import views
from .views import Credit_Profile_Request, credit_profile_form

# URL configuration
urlpatterns = [ 
    path('hello/', views.say_hello),
    path('credit/', views.credit),
    path('credit_profile/', views.credit_profile),
    path('process/', views.process),
    path('Credit_Profile_Request/', Credit_Profile_Request),
    path('main/hello/credit/', views.credit),
    path('dashboard/', views.dashboard),
    path('credit_profile_form/', credit_profile_form),
]