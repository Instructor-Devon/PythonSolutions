from django.shortcuts import render, redirect
from datetime import datetime
from home.game import buildings
import random

GOLD_MAP = {
    "farm": (10,20),
    "cave": (5,10),
    "house": (2,5),
    "casino": (0,50)
}

# Create your views here.
def index(request):
    print('haha')
    if not "gold" in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request, 'index.html', {'buildings': buildings.values()})

def reset(request):
    request.session.clear()
    return redirect('/')

def process_gold(request):
    if request.method == 'GET':
        return redirect('/')
    building = buildings[request.POST['building']]
    result = building.process()
    request.session['activities'].append({"message": result[1], "result": "earn" if result[0] >= 0 else "lose"})
    request.session['gold'] += result[0]
    return redirect('/')
