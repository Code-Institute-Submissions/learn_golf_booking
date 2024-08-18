from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'date', 'time']
        labels = {'name': 'Full Name'}
        widgets = {'date': forms.SelectDateWidget}