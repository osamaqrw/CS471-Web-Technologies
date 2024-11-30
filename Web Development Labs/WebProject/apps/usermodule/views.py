from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def registerUser(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')  # Redirect to login or another page
        else:
            messages.error(request, "Error creating account. Please try again.")
    else:
        form = UserCreationForm()
    return render(request, "usermodule/register.html", {"form": form})
    
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('books.lab9_part2_listbooks')  # Redirect to a page after login
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "usermodule/login.html")

def logoutUser(request):
    logout(request)
    return redirect('login')
