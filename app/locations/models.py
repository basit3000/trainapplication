from django.db import models

class Locations(models.Model):
    name = models.CharField(max_length=64)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)