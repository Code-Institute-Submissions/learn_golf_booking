from django import forms
from .models import Booking

TIME_CHOICES = [(f"{hour:02d}:00", f"{hour:02d}:00") for hour in range(9, 18)]

class BookingForm(forms.ModelForm):
    hire_clubs = forms.BooleanField(required=False, label="Do you need to hire clubs?")
    on_course_lesson = forms.BooleanField(required=False, label="On course lesson? (instead of simulator)")
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone',]
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
        }