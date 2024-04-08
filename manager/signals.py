from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification
from reservation.models import reserv_model

@receiver(post_save, sender=reserv_model)
def create_reservation_notification(sender, instance, created, **kwargs):
    if created:
        # Create a new notification
        Notification.objects.create(message=f'Une nouvelle réservation a été effectuée par {instance.Nom}.', reservation=instance)