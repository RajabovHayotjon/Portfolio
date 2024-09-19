from django.contrib import admin
from .models import Contact
from rest_framework import permissions


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'theme', 'message']
    search_fields = ('name', 'theme')


