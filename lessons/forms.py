from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'date', 'time']
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'date': 'Booking Date',
            'time': 'Booking Time'
        }
        widgets = {
            'date': forms.SelectDateWidget(),
            'time': forms.TimeInput(attrs={'type': 'time'})
        }