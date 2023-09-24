from django.db import models
from .company_model import Company
from django.core.validators import MinValueValidator, MaxValueValidator

class Employee(models.Model):
    JOB_CHOICES = [
        ('software engineer', 'Software Engineer'),
        ('data scientist', 'Data Scientist'),
        ('product manager', 'Product Manager'),
        ('business analyst', 'Business Analyst'),
        ('software developer', 'Software Developer'),
        ('ui/ux designer', 'Ui/UX Designer'), 
        ('manager', 'Manager'),
        ('software tester', 'Software Tester')
    ]
    employeeID = models.BigAutoField(primary_key=True)
    companyID = models.ForeignKey(Company, db_column="companyID", related_name='employees', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    age = models.IntegerField(default=18, validators=[MinValueValidator(18), MaxValueValidator(100)])
    job = models.CharField(max_length=50, choices=JOB_CHOICES, default='software engineer')
    cv = models.CharField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.name + ' - ' + self.email + ' - ' + self.job + ' - ' + self.companyID.name