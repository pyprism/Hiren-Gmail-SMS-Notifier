from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.


def test(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/add')
        else:
            messages.error(request, 'Username/Password is not valid!')
            return redirect(request.path)
    else:
        return redirect('/add')