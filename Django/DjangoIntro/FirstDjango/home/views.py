from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse('INDEX PAGE')

def new(request):
    return HttpResponse('NEW PAGE')

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f'placeholder to display blog number: {number}')

def edit(request, number):
    return HttpResponse(f'placeholder to edit blog number: {number}')

def destroy(request, number):
    return redirect('/')