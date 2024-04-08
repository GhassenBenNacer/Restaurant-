from django.urls import path
from .views import ReservListView
from .views import ReservDetailView , confirm_reservation , AllReservListView ,PendingReservListView ,TodayReservListView

urlpatterns = [
    path('acceuil/', ReservListView.as_view() ,name='list'),
    path('Detail_reservation/<int:pk>/',ReservDetailView.as_view(),name='reserv_detail'),
    path('reservation/<int:pk>/confirm/', confirm_reservation, name='confirm_reservation'),
    path('toutes_reservations',AllReservListView.as_view() ,name='all_reservations'),
    path('reservation-en-attente',PendingReservListView.as_view(),name='reserv_en_attente'),
    path('reservation-du-jour',TodayReservListView.as_view(),name='today_reserv'),

]
