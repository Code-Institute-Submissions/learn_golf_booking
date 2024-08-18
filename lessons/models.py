from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=100, default='Default Name')
    email = models.EmailField(default='example@example.com')
    phone = models.CharField(max_length=15, default='00000000000')
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"