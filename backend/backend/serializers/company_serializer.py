from rest_framework import serializers
from ..models.company_model import Company
from .employee_serializer import EmployeeSerializer

class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = ['companyID', 'name', 'email', 'description']