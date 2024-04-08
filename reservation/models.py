from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
STATUS_CHOICES = (
    ('Pending', 'En attente'),
    ('Accepted', 'Acceptée'),
    ('Rejected', 'Rejetée'),
)

class reserv_model(models.Model):
    Nom=models.CharField(max_length=100, null=False,  error_messages={'required': 'Ce champ est requis.'})
    nbre_person=models.IntegerField(null=False, error_messages={'required': 'Ce champ est requis.'})
    date= models.DateField(null=False, error_messages={'required': 'Ce champ est requis.'})
    heure = models.TimeField(null=False, error_messages={'required': 'Ce champ est requis.'})
    email=models.EmailField(null=False, error_messages={'required': 'Ce champ est requis.'})
    telephone=models.CharField(null=False,max_length=15, error_messages={'required': 'Ce champ est requis.'})
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    def __str__(self):
        return f"{self.Nom} - {self.date} - {self.heure}"

