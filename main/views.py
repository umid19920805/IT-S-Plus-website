from .models import *
from django.shortcuts import render, redirect, HttpResponseRedirect
import requests
from django.contrib.auth import authenticate, login, logout

def index(request):

    return render(request, 'index.html')

def index2(request):

    return render(request, 'index-2.html')

def about(request):

    return render(request, 'about.html')

def blogdetails(request):

    return render(request, 'blog-details.html')

def blog(request):

    return render(request, 'blog.html')

def contact(request):

    return render(request, 'contact.html')

def coursedetails(request):

    return render(request, 'course-details.html')

def courses2(request):

    return render(request, 'courses-2.html')

def courses(request):

    return render(request, 'courses.html')

def faq(request):

    return render(request, 'faq.html')

def index3(request):

    return render(request, 'index-3.html')

def instructorprofile(request):

    return render(request, 'instructor-profile.html')

def instructor(request):

    return render(request, 'instructor.html')

def login(request):

    return render(request, 'login.html')

def price(request):

    return render(request, 'price.html')