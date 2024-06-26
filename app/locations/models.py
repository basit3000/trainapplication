from django.db import models

class Locations(models.Model):
    name = models.CharField(max_length=64)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, default='DE')
    zip_code = models.CharField(max_length=10, default= 00000)

    def __str__(self):
        return self.name