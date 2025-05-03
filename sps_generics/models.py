from django.db import models




class Address(models.Model):
    state = models.CharField(max_length=50)
    lga = models.CharField(max_length=500)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.state}... {self.lga}"
