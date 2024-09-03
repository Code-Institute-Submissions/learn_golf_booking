from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()

    def clean(self):
         if Booking.objects.filter(date=self.date, time=self.time).exclude(id=self.id).exists():
            raise ValidationError("A booking for this date and time already exists.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs) 