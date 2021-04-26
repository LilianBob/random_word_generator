from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    request.session['randomWord']= get_random_string(length=14)
    return render(request, 'index.html')
def generate (request):
    return redirect('/')
def reset(request):
    request.session.flush()
    return redirect ('/')

