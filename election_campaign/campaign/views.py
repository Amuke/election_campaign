from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import MemberForm  # Assuming you have imported MemberForm from your forms.py
from .models import Member  # Assuming you have imported your Member model from models.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

# Custom login view to handle user authentication
def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page or any desired page after login
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid login credentials'})
        else:
            return render(request, 'login.html', {'form': form, 'error': 'Invalid login credentials'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Home view
def home_view(request):
    return render(request, 'home.html')

# User registration view
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Automatically log in the user after registration
            return redirect('home')  # Redirect to the home page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register_user.html', {'form': form})

# Member registration view
def register_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members')  # Redirect to the members page after successful member registration
    else:
        form = MemberForm()
    return render(request, 'register_member.html', {'form': form})

# View to display all members
def members_view(request):
    members = Member.objects.all()
    return render(request, 'members.html', {'members': members})

# Logout view
def logout_view(request):
    logout(request)  # Log out the user
    return redirect('login')  # Redirect to the login page after logout
