from django.db import models

class Tickets(models.Model):
    name = models.CharField(max_length=24)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(help_text="Duration in days", default=1)

    def __str__(self):
        return self.name
    
class UserTickets(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    issue_date = models.DateField()
    expiry_date = models.DateField()

    