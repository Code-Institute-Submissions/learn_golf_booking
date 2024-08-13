from django.db import models

# Create your models here.

class Booking(models.Model):
    customer_name = models.CharField(max_length=50)
    booking_date = models.DateField()
    booking_time = models.TimeField()

    def __str__(self):
        return f"Booking {self.id} by {self.customer_name} on {self.booking_date} at {self.booking_time}"