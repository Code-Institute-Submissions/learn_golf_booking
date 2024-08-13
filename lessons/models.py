from django.db import models

# Create your models here.

class Booking(models.Model):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String(100), nullable=False)
    booking_date = Column(Date, nullable=False)
    booking_time = Column(Time, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    def __repr__(self):
        return f"<Booking(id={self.id}, customer_name={self.customer_name}, date={self.booking_date}, time={self.booking_time})>"
