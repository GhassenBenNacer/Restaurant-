from django.db import models
from django.urls import reverse
from reservation.models import reserv_model

class Notification(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    reservation = models.ForeignKey(reserv_model, on_delete=models.CASCADE,default =None)

    class Meta:
        app_label = 'manager'
