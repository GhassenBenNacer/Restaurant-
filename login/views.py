from django.shortcuts import render , redirect 
from django.contrib.auth import authenticate , login , logout
from login.forms import UpdateUser , ChangePassword
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.


def login_user(request):
    error_message = None
    if request.method =='POST':

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            error_message = "Nom d'utilisateur ou mot de passe incorrect"  # Set error message
            # Render the login page again with an error message
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request ,'login.html',{})

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UpdateUser(request.POST, instance=request.user)

        if user_form.is_valid() :
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('list')
    else:
        user_form = UpdateUser(instance=request.user)

    return render(request, 'modifier.html', {'user_form': user_form})

@login_required
def update_password(request):
    if request.method == 'POST':
        form = ChangePassword(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Votre mot de passe est modifie avec succes')
            return redirect('login')
        else:
            messages.error(request, 'Essayez de mettre un mot de passe plus fort!')
    else:
        form = ChangePassword(request.user)
    return render(request, 'modifier_mdp.html', {'form': form})
