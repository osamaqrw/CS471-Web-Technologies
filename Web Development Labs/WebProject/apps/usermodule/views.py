from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import logout

def registerUser(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            obj = form.save()
            # should we say something here: comes next using messages
            return redirect('login')
    form = SignUpForm()
    return render(request, "usermodule/register.html", {"form": form})

def loginUser(request):
    return redirect(request, 'bookmodule/list_books.html')

def logoutUser(request):
    logout(request)
    return redirect(request, 'bookmodule/list_books.html')
