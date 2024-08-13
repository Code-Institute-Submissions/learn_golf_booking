from django.shortcuts import render
from django.http import HttpResponse
from models import Booking

# Create your views here.

def booking_create(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return redirect('booking_detail', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, '', {'form': form})

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