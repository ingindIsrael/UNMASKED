from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from users.models import Profile

from django.db.utils import IntegrityError


def update_profile(request):
    return render(request, 'users/update_profile.html')
    

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('feed')
        else: 
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})
    return render(request, 'users/login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error':'Password confirmation does not mach'})

        try:
            user = User.objects.create_user(username=username, password=passwd)
        except:
            return render(request, 'users/signup.html', {'error':'Username is used already'})
        
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email= request.POST['email']

        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')