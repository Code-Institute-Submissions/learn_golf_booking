from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_lessons, name='book_lessons'),
    path('success/', views.success, name='success'),
]