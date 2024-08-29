from django.utils import timezone
from .models import Booking

class DeletePastBookingsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        today = timezone.now().date()
        Booking.objects.filter(date__lt=today).delete()

        response = self.get_response(request)
        return response