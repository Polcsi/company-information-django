from rest_framework import serializers
from models.employee_model import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('employeeID', 'name', 'email', 'description', 'companyID')