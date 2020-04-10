from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class AddQues(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class UpdateProfilePic(ModelForm):
    class Meta:
        model = Leader
        fields = '__all__'
        exclude = ['user','score']    

class UpdateUser(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']            


