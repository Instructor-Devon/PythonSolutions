from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if "count" not in request.session:
        request.session['count'] = 0

    return render(request, 'index.html')

def get_clicks(request):
    return HttpResponse(request.session['count'], content_type='application/json')

def set_clicks(request):
    request.session['count'] += 1
    return redirect('/clicks/get')