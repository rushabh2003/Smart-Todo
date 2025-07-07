

# Create your models here.
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    deadline = models.DateField(null=True, blank=True)
    priority = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)

class ContextEntry(models.Model):
    source = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
