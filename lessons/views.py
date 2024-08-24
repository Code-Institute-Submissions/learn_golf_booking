from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking

@login_required
def book_lessons(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = BookingForm()
    return render(request, 'lessons/book_lessons.html', {'form': form})

def success(request):
    return render(request, 'lessons/success.html')

@login_required
def booking_create(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return redirect('booking_detail', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'lessons/book_lessons.html', {'form': form})

@login_required
def booking_update(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save()
            return redirect('booking_detail', booking_id=booking.id)
    else:
        form = BookingForm(instance=booking)
    return render(request, 'lessons/booking_form.html', {'form': form})

@login_required
def booking_delete(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == "POST":
        booking.delete()
        return redirect('booking_list')
    return render(request, 'lessons/booking_confirm_delete.html', {'booking': booking})