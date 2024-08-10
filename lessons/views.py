from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def book_lessons(request):
    return HttpResponse("Book a lesson!")