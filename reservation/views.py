from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import reserv_model 
from .forms import reservation_form
# Create your views here.

from django.shortcuts import render


def reserv_sent(request):
    return render(request ,"reservationenv.html")

def reserv_view(request):
    form = reservation_form()
    if request.method == "POST":
        form = reservation_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reserv_sent') 
    else:
        form = reservation_form()
    
    context = {'form': form}
    return render(request, 'index.html', context)





