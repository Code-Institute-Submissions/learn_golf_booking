from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking

@login_required
def book_lessons(request):
    if request.method == 'POST':
        if 'delete_booking_id' in request.POST: 
            booking_id = request.POST.get('delete_booking_id')
            booking_to_delete = get_object_or_404(Booking, id=booking_id, user=request.user)
            booking_to_delete.delete()
            return redirect('book_lessons')
        else:
            if 'booking_id' in request.POST:  
                booking = get_object_or_404(Booking, id=request.POST['booking_id'], user=request.user)
                form = BookingForm(request.POST, instance=booking)
            else: 
                form = BookingForm(request.POST)
            
            if form.is_valid():
                booking = form.save(commit=False)
                booking.user = request.user
                booking.save()
                return redirect('book_lessons')
    else:
        form = BookingForm()

    bookings = Booking.objects.filter(user=request.user)

    return render(request, 'lessons/book_lessons.html', {
        'form': form,
        'bookings': bookings,
    })
def home(request):
    return render(request, 'book_lessons.html')

def success(request):
    return render(request, 'lessons/success.html')

@login_required
def booking_update(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('book_lessons')  #
    else:
        form = BookingForm(instance=booking)

    return render(request, 'lessons/book_lessons.html', {
        'form': form,
        'editing': True,
        'booking_id': booking_id,
        'bookings': Booking.objects.filter(user=request.user),
    })
@login_required
def booking_delete(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == "POST":
        if 'confirm_delete' in request.POST:
            booking.delete()
            return redirect('book_lessons')

    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'lessons/book_lessons.html', {
        'bookings': bookings,
        'delete_confirmation': True,  
        'booking_to_delete': booking,  
    })