from django.shortcuts import render, get_object_or_404 , redirect
from django.views.generic import ListView, DetailView
from reservation.models import reserv_model
from django.utils import timezone
from datetime import datetime, timedelta ,date
from django.db.models import Count, Avg
from .models import Notification
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator






class ReservListView(LoginRequiredMixin, ListView):
    model = reserv_model
    template_name = 'list.html'
    context_object_name = 'reservations'
    paginate_by = 5  # Number of reservations per page

    def get_queryset(self):
        # Get the queryset filtered by date greater than or equal to now
        queryset = super().get_queryset().filter(date__gte=timezone.now()).order_by('date')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_date = timezone.now().date()

        # Calculate statistics
        all_reservations = self.get_queryset()
        today_reservations = all_reservations.filter(date=current_date)
        not_confirmed_reservations = all_reservations.filter(status='Pending')
        mean_clients_per_reservation = all_reservations.aggregate(Avg('nbre_person'))

        # Convert the mean number of clients per reservation to an integer
        mean_clients_per_reservation_int = int(mean_clients_per_reservation['nbre_person__avg'] or 0)

        # Add statistics to the context
        context['total_reservations'] = all_reservations.count()
        context['today_reservations'] = today_reservations.count()
        context['not_confirmed_reservations'] = not_confirmed_reservations.count()
        context['mean_clients_per_reservation'] = mean_clients_per_reservation_int
        context['current_date'] = current_date

        # Retrieve notifications
        notifications = Notification.objects.all().order_by('-created_at')
        context['notifications'] = notifications

        return context

    def post(self, request, *args, **kwargs):
        if 'delete_all' in request.POST:
            # Delete all notifications
            Notification.objects.all().delete()
        return redirect('list')

class AllReservListView(LoginRequiredMixin ,ListView):
    model = reserv_model
    template_name = 'all_reservation.html'
    context_object_name = 'allReservations'

    def get_queryset(self):
        queryset = super().get_queryset()

        # Get filter parameters from the URL query string
        status = self.request.GET.get('status')
        order = self.request.GET.get('order')

        # Apply status filter
        if status:
            queryset = queryset.filter(status=status)

        # Apply date filter
        if order == 'date_asc':
            queryset = queryset.order_by('date')
        elif order == 'date_desc':
            queryset = queryset.order_by('-date')

        return queryset



class ReservDetailView(LoginRequiredMixin ,DetailView):
    model = reserv_model
    template_name = 'reserv_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reservation = self.get_object()

        if reservation.status == 'Accepted':
            context['accepted'] = True
        else:
            context['accepted'] = False

        # Fetch other reservations on the same date
        reservations_same_date_accepted = reserv_model.objects.filter(date=reservation.date, status='Accepted')

        context['reservations_same_date_accepted'] = reservations_same_date_accepted

        return context



@login_required
def confirm_reservation(request, pk):
    reservation = get_object_or_404(reserv_model, pk=pk)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'confirm':
            reservation.status = 'Accepted'
        elif action == 'reject':
            reservation.status = 'Rejected'
        
        reservation.save()
        
        return redirect('list')  # Assuming 'list' is the name of the view you want to redirect to after confirmation/rejection
    
    return render(request, 'reserv_detail.html', {'reservation': reservation})

class PendingReservListView(LoginRequiredMixin ,ListView):
    model = reserv_model
    template_name = 'pending_reservation.html'
    context_object_name = 'pendingReservations'

    def get_queryset(self):
        return reserv_model.objects.filter(status='Pending')



class TodayReservListView(LoginRequiredMixin ,ListView):
    model = reserv_model
    template_name = 'today_reservation.html'
    context_object_name = 'todayReservations'

    def get_queryset(self):
        today = timezone.now().date()
        return reserv_model.objects.filter(date=today)
















    
