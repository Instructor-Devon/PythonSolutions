from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def generate_word():
    return get_random_string(length=13).upper()

# Create your views here.
def index(request):
    # check if session has been initialized
    if 'attempts' not in request.session:
        request.session['attempts'] = 1
        request.session['word'] = generate_word()
    return render(request, 'index.html')

def generate(request):
    request.session['attempts'] += 1
    request.session['word'] = generate_word()
    return redirect('/')
