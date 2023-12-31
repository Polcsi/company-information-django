from django.db import models

class Company(models.Model):
    companyID = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    description = models.CharField(max_length=500,blank=True, null=True)
    
    def __str__(self):
        return self.name + " (" + str(self.companyID) + ")"