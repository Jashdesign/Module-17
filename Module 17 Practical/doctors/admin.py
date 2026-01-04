from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'specialization',
        'phone',
        'experience_years',
        'is_active',
    )
    search_fields = ('name', 'specialization')
    list_filter = ('specialization', 'is_active')