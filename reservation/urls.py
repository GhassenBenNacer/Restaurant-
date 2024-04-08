from django.urls import path
from .views import reserv_view , reserv_sent

urlpatterns = [
    path('reservation_envoyee', reserv_sent, name='reserv_sent'),
    path('',reserv_view, name='reserv_view'),
]
