from django import forms
from .models import Booking

TIME_CHOICES = [(f"{hour:02d}:00", f"{hour:02d}:00") for hour in range(9, 18)]

class BookingForm(forms.ModelForm):
    hire_clubs = forms.BooleanField(required=False, label="Do you need to hire clubs?")
    on_course_lesson = forms.BooleanField(required=False, label="On course lesson (instead of simulator)")
    date = forms.DateField(widget=forms.HiddenInput())
    time = forms.ChoiceField(choices=TIME_CHOICES, widget=forms.HiddenInput())

    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'date', 'time', 'hire_clubs', 'on_course_lesson']
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
        }
    
    date = forms.DateField(widget=forms.HiddenInput(), required=False)
    time = forms.TimeField(widget=forms.HiddenInput(), required=False)
