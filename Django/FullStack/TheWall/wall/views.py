from django.shortcuts import render, redirect
from django.contrib import messages
from logreg.models import User
from wall.models import Message, Comment
# Create your views here.
def index(request):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'posts': Message.objects.order_by('-created_at')
    }
    return render(request, 'wall/index.html', context)

def create_message(request):
    errors = Message.objects.validate(request.POST)
    if errors:
        for e in errors:
            messages.error(request, e)
    else:
        Message.objects.create(
            content = request.POST['content'],
            author_id = request.POST['user_id'],
        )
    return redirect('/wall')

def create_comment(request):
    errors = Comment.objects.validate(request.POST)
    if errors:
        for e in errors:
            messages.error(request, e)
    else:
        Comment.objects.create(
            content = request.POST['content'],
            author_id = request.POST['user_id'],
            message_id = request.POST['message_id']
        )
    return redirect('/wall')