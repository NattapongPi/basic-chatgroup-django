from django.contrib import admin

from .models import Message,Room

admin.site.register(Room)
admin.site.register(Message)