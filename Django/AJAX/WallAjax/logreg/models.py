from django.db import models
from django.core.validators import validate_email
import bcrypt
class UserManager(models.Manager):
    def validate(self, form):
        errors = []
        if len(form['first_name']) < 3:
            errors.append('First Name must be at least 3 characters')

        if len(form['last_name']) < 3:
            errors.append('Last Name must be at least 3 characters')

        try:
            validate_email(form['email'])
        except:
            errors.append('Invalid Email Address')
        
        email_check = self.filter(email=form['email'])
        if email_check:
            errors.append("Email already in use")

        if len(form['password']) < 8:
            errors.append('Password must be at least 8 characters')
        
        return errors
    
    def authenticate(self, email, password):
        user = None
        try: 
            user = User.objects.get(email=email)
        except:
            return False
        return bcrypt.checkpw(password.encode(), user.password.encode())

    def register(self, form):
        pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name = form['first_name'],
            last_name = form['last_name'],
            email = form['email'],
            password = pw,
        )
        
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    objects = UserManager()