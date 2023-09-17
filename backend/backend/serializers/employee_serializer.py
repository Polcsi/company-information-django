from rest_framework import serializers
from ..models.employee_model import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('employeeID', 'companyID', 'name', 'email', 'age', 'job', 'cv')
        
# Serializer without the companyID field
class EmployeeCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employeeID', 'name', 'email', 'age', 'job']
        extra_kwargs = {'employeeID': {'read_only': False, "required": False}}