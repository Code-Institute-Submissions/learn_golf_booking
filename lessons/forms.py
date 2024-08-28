from django import forms
from .models import Booking

TIME_CHOICES = [(f"{hour:02d}:00", f"{hour:02d}:00") for hour in range(9, 18)]

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone',]
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
        }