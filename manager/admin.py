from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['message', 'created_at', 'is_read', 'reservation']  # Add 'reservation' to the list display
    list_filter = ['is_read']
    search_fields = ['message']
    readonly_fields = ['created_at', 'is_read', 'reservation'] 