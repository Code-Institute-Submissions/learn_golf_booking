"""
URL configuration for codestar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from lessons import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('book/', views.book_lessons, name='book_lessons'),
    path('booking/<int:booking_id>/edit/', views.booking_update, name='booking_update'),
    path('bookings/delete/<int:booking_id>/', views.booking_delete, name='booking_delete'),
    path('success/', views.success, name='success'),
    path('', views.home, name='home'),
    path('available-slots/', views.available_slots, name='available_slots'),
    path('careers/', views.careers_view, name='careers'), 
    path('gallery/', views.gallery_view, name='gallery'),
    path('lessons/', include('lessons.urls')), 
]
