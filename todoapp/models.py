from django.db import models

class Todo(models.Model):
    summary = models.CharField(max_length=100)
    details = models.TextField(blank=True)
    done = models.BooleanField()
