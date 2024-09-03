from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.dateparse import parse_date
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from .forms import BookingForm
from .models import Booking
from django.utils import timezone
from django.core.exceptions import ValidationError

def available_slots(request):
    date_str = request.GET.get('date')
    date = parse_date(date_str)

    if date:
        booked_times = Booking.objects.filter(date=date).values_list('time', flat=True)
        all_times = [
            "09:00", "10:00", "11:00", "12:00", "13:00",
            "14:00", "15:00", "16:00", "17:00"
        ]
        booked_times = [bt.strftime('%H:%M') for bt in booked_times]

        available_times = [time for time in all_times if time not in booked_times]
        return JsonResponse(available_times, safe=False)
    else:
        return JsonResponse([], safe=False)

@receiver(user_logged_in)
def delete_past_bookings_on_login(sender, request, user, **kwargs):
    today = timezone.now().date()
    Booking.objects.filter(date__lt=today).delete()

def delete_past_bookings():
    today = timezone.now().date()
    Booking.objects.filter(date__lt=today).delete()

@require_http_methods(["GET", "POST"])
@login_required
def book_lessons(request):
    delete_past_bookings()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        selected_date = request.POST.get('selected_date')
        selected_time = request.POST.get('selected_time')

        if form.is_valid() and selected_date and selected_time:
            selected_date_obj = parse_date(selected_date)

            if selected_date_obj and selected_date_obj < timezone.now().date():
                form.add_error(None, 'You cannot book a date in the past.')
            else:
                booking = form.save(commit=False)
                booking.user = request.user
                booking.date = selected_date
                booking.time = selected_time if len(selected_time.split(':')) == 3 else f"{selected_time}:00"
                booking.hire_clubs = form.cleaned_data.get('hire_clubs', False)
                booking.on_course_lesson = form.cleaned_data.get('on_course_lesson', False)

                try:
                    booking.save()
                    print("Booking saved successfully.") 
                    return redirect('book_lessons')
                except ValidationError as e:
                    print("Validation error during save:", e)
                    form.add_error(None, e)
        else:
            print("Form validation failed:", form.errors) 

    else:
        form = BookingForm()

    bookings = Booking.objects.filter(user=request.user)
    print("Bookings retrieved:", bookings) 
    return render(request, 'lessons/book_lessons.html', {'form': form, 'bookings': bookings})

    bookings = Booking.objects.filter(user=request.user)
    print("Bookings retrieved:", bookings) 
    return render(request, 'lessons/book_lessons.html', {'form': form, 'bookings': bookings})

@login_required
def success(request):
    return render(request, 'lessons/success.html')

def home(request):
    return render(request, 'lessons/book_lessons.html') 

@login_required
@login_required
def booking_update(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)  
        selected_date = request.POST.get('selected_date')
        selected_time = request.POST.get('selected_time')

        if form.is_valid() and selected_date and selected_time:
            selected_date_obj = parse_date(selected_date)

            if selected_date_obj and selected_date_obj < timezone.now().date():
                form.add_error(None, 'You cannot book a date in the past.')
            else:
                booking.date = selected_date_obj
                booking.time = selected_time
                booking.hire_clubs = form.cleaned_data.get('hire_clubs', False)
                booking.on_course_lesson = form.cleaned_data.get('on_course_lesson', False)
                
                try:
                    booking.save()
                    print("Booking successfully updated.")
                    return redirect('book_lessons') 
                except ValidationError as e:
                    print("Validation error during update:", e)
                    form.add_error(None, e)
        else:
            print("Update failed due to form errors:", form.errors)
    else:
        form = BookingForm(instance=booking)

    return render(request, 'lessons/book_lessons.html', {'form': form, 'editing': True, 'booking_id': booking_id})


@login_required
def booking_delete(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == "POST":
        booking.delete()
        print(f"Booking {booking_id} successfully deleted.") 
        return redirect('book_lessons')

    return redirect('book_lessons')
