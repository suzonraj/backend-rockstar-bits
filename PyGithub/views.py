from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.
from PyGithub.forms import SignUpForm


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return render(request, 'home.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.username = username
            user.password = password
            user.save()

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = SignUpForm(request.POST)
        return render(request, 'registration/signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('/')
