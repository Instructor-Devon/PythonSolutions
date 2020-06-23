from django.db import models
from logreg.models import User
# Create your models here.

class MessageManager(models.Manager):
    def validate(self, form):
        errors = []
        if len(form['content']) < 5:
            errors.append('Wall post must be 5 or more characters')
        return errors

class CommentManager(models.Manager):
    def validate(self, form):
        errors = []
        if len(form['content']) < 5:
            errors.append('Wall post must be 5 or more characters')
        return errors

class Message(models.Model):
    content = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MessageManager()

    def comments_by_date(self):
        return self.comments.order_by('-created_at')

class Comment(models.Model):
    content = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CommentManager()