from django.db import models

# Create your models here.

class Search(models.Model):
    address_location = models.CharField(max_length=250, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address_location
