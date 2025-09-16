from tkinter.constants import CASCADE
from django.contrib.auth.forms import User
from django.db import models


class User_model(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_photo = models.ImageField(upload_to='media/', null=True)

class Category(models.Model):
    category_name = models.CharField(max_length=32)
    category_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Категории'


class New(models.Model):
    new_name = models.CharField(max_length=128)
    new_desc = models.TextField()
    new_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    new_photo = models.ImageField(upload_to='media/', blank=True, null=True)
    new_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.new_name

    class Meta:
        verbose_name_plural = 'Новости'