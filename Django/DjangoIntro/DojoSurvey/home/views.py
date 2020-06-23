from django.shortcuts import render, redirect
LANGS = (
    'Python',
    'JavaScript',
    'C#',
    'Java',
    'C++'
)
LOCATIONS = (
    'San Jose',
    'Seattle',
    'Chicago',
    'Online'
)

# Create your views here.
def index(request):
    context = {
        'locations': LOCATIONS,
        'languages': LANGS
    }
    return render(request, 'index.html', context)

def result(request):
    if request.method == 'GET':
        return redirect('/')
    context = {
        'result': request.POST
    }
    return render(request, 'result.html', context)

