from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course
# Create your views here.
def index(request):
    if request.method == "POST":
        errors = Course.objects.validate(request.POST)
        if errors:
            for e in errors:
                messages.error(request, e)
        else:
            Course.objects.create_course(request.POST)
        return redirect("/")
    context = {
        "courses": Course.objects.all()
    }
    return render(request, "index.html", context)

def delete(request, course_id):
    course_to_delete = Course.objects.filter(id=course_id)
    course_to_delete.delete()
    return redirect("/")

def confirm(request, course_id):
    context = {
        "course": Course.objects.get(course_id)
    }
    return render(request, "confirm.html", context)