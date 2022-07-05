from distutils.command.upload import upload
from email.mime import image
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="My Awesome Blog!")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    small_desc = models.TextField()
    full_desc = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)) )
        return reverse('home')