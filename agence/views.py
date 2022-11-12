from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login_user(request):
    messages_text = "L'utilisateur renseigné n'est pas correcte, veuillez réessayez svp"
    if request.method =="POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, messages_text)
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def about(request):
    return render(request, 'about.html')
