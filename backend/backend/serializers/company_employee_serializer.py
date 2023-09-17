from rest_framework import serializers
from ..models.company_model import Company
from ..models.employee_model import Employee
from .employee_serializer import EmployeeCompanySerializer

class CompanyEmployeeSerializer(serializers.ModelSerializer):
    # Serialize the employees of a company
    employees = EmployeeCompanySerializer(many=True)
    
    class Meta:
        model = Company
        fields = ['companyID', 'name', 'email', 'description', 'employees']
    
        
    def create(self, validated_data):
        employees_data = validated_data.pop('employees')
        company = Company.objects.create(**validated_data)
        
        for employee_data in employees_data:
            Employee.objects.create(companyID=company, **employee_data)
        
        return company
    
    def update(self, instance, validated_data):
        employees_data = validated_data.pop('employees')
        
        # Update the company informations
        instance[0].name = validated_data.get('name', instance[0].name)
        instance[0].email = validated_data.get('email', instance[0].email)
        instance[0].description = validated_data.get('description', instance[0].description)
        instance[0].save()
        
        # Update the employees
        keep_employees = []
        existing_ids = [employee.employeeID for employee in instance[0].employees.all()]
        for employee_data in employees_data:
            print(employee_data)
            if 'employeeID' in employee_data.keys():
                if Employee.objects.filter(employeeID=employee_data['employeeID']).exists():
                    print("Employee exists")
                    # Update the existing employee
                    employee = Employee.objects.get(employeeID=employee_data['employeeID'])
                    employee.name = employee_data.get('name', employee.name)
                    employee.email = employee_data.get('email', employee.email)
                    employee.age = employee_data.get('age', employee.age)
                    employee.job = employee_data.get('job', employee.job)
                    employee.cv = employee_data.get('cv', employee.cv)
                    employee.save()
                    # Add the employee to the list of employees to keep
                    keep_employees.append(employee.employeeID)
                else:
                    continue
            else:
                # Create a new employee
                employee =  Employee.objects.create(companyID=instance[0], **employee_data)
                keep_employees.append(employee.employeeID)
        
        # Delete the employees that are not in the request
        for employee in instance[0].employees.all():
            if employee.employeeID not in keep_employees:
                employee.delete()
            
        # Update the company informations
        return instance[0]
        