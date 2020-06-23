from django.db import models

class CourseManager(models.Manager):
    def validate(self, data):
        errors = []
        if(len(data['name']) < 3):
            errors.append("Name is too short")

        if(len(data['name']) < 5):
            errors.append("Description is too short")
        
        return errors
    def create_course(self, data):
        return self.create(
            name = data['Name'],
            description = data['Description']
        )

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()