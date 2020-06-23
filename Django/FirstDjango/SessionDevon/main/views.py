from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    # POSTS ONLY
    if request.method != "POST":
        return redirect("/")
    
    # see if there's errors
    errors = User.objects.validate(request.POST)

    # if there's at least one thing in this list
    if errors:
        for err in errors:
            messages.error(request, err)
        return redirect("/")
    
    # no errors, register da user
    new_user = User.objects.register(request.POST)
    
    # log EM IN!
    request.session["id"] = new_user.id

    return redirect("/success")

def login(request):
    # POSTS ONLY
    if request.method != "POST":
        return redirect("/")

    if not User.objects.authenticate(request.POST["email"], request.POST["password"]):
        messages.error(request, "Invalid Credentials")
        return redirect("/")
    
    # LOG EM IN!
    # get user now
    user = User.objects.get(email=request.POST["email"])
    request.session["id"] = user.id
    return redirect("/success")

def success(request):
    user = User.objects.get(id=request.session["id"])
    return HttpResponse(f"SUCCESS {user.first_name}")