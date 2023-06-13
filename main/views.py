from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import ContactForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        message = request.POST.get('message')
        form = ContactForm(name=name, email=email, phonenumber=phonenumber, message=message)
        form.save()

    return render(request, 'food/index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User = UserForm(username=username, email=email, password=password)
        User.Create()
        User.save()

    return render(request, 'main/signup.html')


@csrf_exempt
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(username=username, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')    
            else:
                return render(request, 'main/login.html')
          
    return render(request, 'main/login.html')


def logoutUser(request):
    logout(request)
    return HttpResponse('<h1>You Are Logged Out</h1>')