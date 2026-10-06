from django.contrib import admin
from .models import Hostel


@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'hostel_type',
        'rent',
        'distance',
        'food_available',
        'available_beds',
        'rating',
    )

    list_filter = (
        'hostel_type',
        'food_available',
    )

    search_fields = (
        'name',
        'location',
    )