from django.db import models
from django.utils import timezone

class Hostel(models.Model):

    HOSTEL_TYPES = [
        ('Boys', 'Boys'),
        ('Girls', 'Girls'),
    ]

    name = models.CharField(max_length=100)
    hostel_type = models.CharField(max_length=10, choices=HOSTEL_TYPES)
    location = models.CharField(max_length=200)

    rent = models.IntegerField()

    distance = models.CharField(
        max_length=100,
        default="Not specified"
    )

    food_available = models.BooleanField(default=False)

    total_beds = models.IntegerField(default=0)
    available_beds = models.IntegerField(default=0)

    phone = models.CharField(max_length=15)

    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=0
    )

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name