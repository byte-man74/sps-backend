from django.db import models





class SchoolOnboarding(models.Model):
    """this would be the model responsible for storing information about schools pre registering on the platform"""

    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="onboarding_logo")
    address = models.ForeignKey("sps_generics.Address", on_delete=models.CASCADE)
    contact_information = 

    def __str__(self):
        return self.name
