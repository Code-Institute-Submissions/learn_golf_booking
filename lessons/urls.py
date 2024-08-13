from django.urls import path
from . import views

urlpatterns = [
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('bookings/new/', views.booking_create, name='booking_create'),
    path('bookings/<int:booking_id>/edit/', views.booking_update, name='booking_update'),
    path('bookings/<int:booking_id>/delete/', views.booking_delete, name='booking_delete'),
]