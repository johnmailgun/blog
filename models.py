from django.db import models
from django.shortcuts import render
from django.urls import reverse
from django_quill.fields import QuillField


# Create your models here.
class Post(models.Model):
    head = models.CharField(max_length=200)
    text = QuillField()

    def __str__(self):
        return self.head
    
    def get_absolute_url(self):
        return reverse('index')