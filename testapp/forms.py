from django import forms
from django.contrib.auth.forms import UserCreationForm, User

from .models import New, User_model, Category


class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ['new_name', 'new_desc', 'new_category', 'new_photo']

class NewCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']

class Users(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User_model
        fields = ["user_photo"]



class AvatarForm(forms.ModelForm):
    class Meta:
        model = User_model
        fields = ["user_photo"]
