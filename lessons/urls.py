from django.urls import path, reverse
from . import views

urlpatterns = [
    path('book/', views.book_lessons, name='book_lessons'),  
    path('booking/<int:booking_id>/edit/', views.booking_update, name='booking_update'),
    path('booking/<int:booking_id>/delete/', views.booking_delete, name='booking_delete'),
    path('success/', views.success, name='success'), 
    path('', views.home, name='home'),
    path('available-slots/', views.available_slots, name='available_slots'),
]