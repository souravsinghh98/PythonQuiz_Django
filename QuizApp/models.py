from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    ques = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct = models.CharField(max_length=200)

    def __str__(self):
        return self.ques

class Leader(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    score = models.IntegerField(null=True)
    profile = models.ImageField(default='default_pic.png', null=True, blank=True)

    def __str__(self):
        return self.user.first_name

    

    


    
