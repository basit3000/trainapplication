from django.db import models

class Tickets(models.Model):
    name = models.CharField(max_length=24)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)