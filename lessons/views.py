from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookingForm

# Create your views here.

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

def booking_create(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return redirect('booking_detail', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'book_lessons.html', {'form': form})

def booking_update(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save()
            return redirect('booking_detail', booking_id=booking.id)
    else:
        form = BookingForm(instance=booking)
    return render(request, '', {'form': form})

def booking_delete(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == "POST":
        booking.delete()
        return redirect('booking_list')
    return render(request, '', {'booking': booking})