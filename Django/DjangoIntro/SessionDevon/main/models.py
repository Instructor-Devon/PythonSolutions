from django.db import models
import re
import bcrypt
EMAIL_REG = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    # custom methods!
    
    def validate(self, post_data):
        errors = []
        # find errors, add to errors list
        if len(post_data["first_name"]) < 3:
            errors.append("Name fields must be 3 or more")
        elif len(post_data["last_name"]) < 3:
            errors.append("Name fields must be 3 or more")
        if not EMAIL_REG.match(post_data["email"]):
            errors.append("Invalid Email")
        if len(post_data["password"]) < 8:
            errors.append("Passwords must be at least 8")
        if post_data["password"] != post_data["confirm"]:
            errors.append("Passwords do not match!")
        return errors
    
    def register(self, post_data):
        # Create a user, but hash password first!
        hashed = bcrypt.hashpw(post_data["password"].encode(), bcrypt.gensalt()).decode()

        # return new user
        # User.objects == self (here)
        return self.create(
            first_name = post_data["first_name"],
            last_name = post_data["last_name"],
            email = post_data["email"],
            password = hashed
        )
    
    def authenticate(self, email, password):
        # return True/False... is this person who they say they are!

        # is the email in the system?
        # User.objects == self (here)
        user_attempt = self.filter(email=email)
        # this will be emtpy list if email not in system
        if len(user_attempt) < 1:
            return False
        
        user = user_attempt[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())
        # if so... does the password match (password for user with email)


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    # 2dlkflswjr32li4jrl24kjflksjdlkfjsdlkfjl24
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()