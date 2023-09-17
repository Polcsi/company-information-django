from rest_framework import serializers
from ..models.employee_model import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('employeeID', 'companyID', 'name', 'email', 'age', 'job', 'cv')
        read_only_fields = ['companyID']
        
# Serializer without the companyID field
class EmployeeCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employeeID', 'name', 'email', 'age', 'job']
        read_only_fields = ['employeeID']