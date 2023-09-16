from django.contrib import admin
from .models.company_model import Company
from .models.employee_model import Employee

admin.site.register(Company)
admin.site.register(Employee)
# admin.site.register(Employee)