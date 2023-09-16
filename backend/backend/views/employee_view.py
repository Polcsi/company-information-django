from django.http import JsonResponse
from ..models.employee_model import Employee
from ..serializers.employee_serializer import EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def employee_list(request, format=None):
    if request.method == 'GET':
        # get all employees from the database
        employees = Employee.objects.all()
        # serialize the employees
        serializer = EmployeeSerializer(employees, many=True)
        # return the serialized data
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        # create a new employee from the request data
        serializer = EmployeeSerializer(data=request.data)
        # check if the data is valid
        if serializer.is_valid():
            # save the new employee to the database
            serializer.save()
            # return the serialized data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return an error if the data is not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, id, format=None):
    try:
        # get the employee from the database
        employee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        # return an error if the employee does not exist
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        # serialize the employee
        serializer = EmployeeSerializer(employee)
        # return the serialized data
        return Response(serializer.data)
    
    if request.method == 'PUT':
        # update the employee with the request data
        serializer = EmployeeSerializer(employee, data=request.data)
        # check if the data is valid
        if serializer.is_valid():
            # save the updated employee to the database
            serializer.save()
            # return the serialized data
            return Response(serializer.data)
        # return an error if the data is not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        # delete the employee from the database
        employee.delete()
        # return a success message
        return Response(status=status.HTTP_204_NO_CONTENT)