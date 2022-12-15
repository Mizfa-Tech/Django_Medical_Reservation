from django.contrib import admin
from .models import *
from django_jalali.admin.filters import JDateFieldListFilter
# Register your models here.
import django_jalali.admin as jadmin

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_filter = (
        ('datetime', JDateFieldListFilter),
    )

admin.site.register(Prescription)

