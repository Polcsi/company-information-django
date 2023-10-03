from django.http import JsonResponse
from ..models.company_model import Company
from ..serializers.company_serializer import CompanySerializer
from ..serializers.company_employee_serializer import CompanyEmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def company_list(request, format=None):
    if request.method == 'GET':
        # get all companies from the database
        companies = Company.objects.all()
        # serialize the companies
        serializer = CompanySerializer(companies, many=True)
        # return the serialized data
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        # create a new company from the request data
        serializer = CompanySerializer(data=request.data)
        # check if the data is valid
        if serializer.is_valid():
            # save the new company to the database
            serializer.save()
            # return the serialized data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return an error if the data is not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def company_detail(request, id, format=None):
    try:
        # get the company from the database
        company = Company.objects.get(pk=id)
    except Company.DoesNotExist:
        # return a 404 if the company does not exist
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        # serialize the company
        serializer = CompanySerializer(company)
        # return the serialized data
        return Response(serializer.data)
    
    if request.method == 'PUT':
        # update the company with the request data
        serializer = CompanySerializer(company, data=request.data, partial=False)
        # check if the data is valid
        if serializer.is_valid():
            # save the updated company to the database
            serializer.save()
            # return the serialized data
            return Response(serializer.data)
        # return an error if the data is not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        # delete the company from the database
        company.delete()
        # return a 204 response
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'PUT'])
def company_employees(request, id, format=None):
    try:
        # get the company from the database
        company = Company.objects.filter(companyID=id)
    except Company.DoesNotExist:
        # return a 404 if the company does not exist
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        # serialize the employees
        serializer = CompanyEmployeeSerializer(company, many=True)
        # return the serialized data
        return Response(serializer.data)
    if request.method == 'PUT':
        # update the company with the request data
        serializer = CompanyEmployeeSerializer(company, data=request.data)
        # check if the data is valid
        if serializer.is_valid():
            # save the updated company to the database
            serializer.save()
            # return the serialized data
            return Response(serializer.data)
        # return an error if the data is not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def company_add_employee(request, format=None):
    if request.method == 'POST':
        # create a new employee from the request data
        serializer = CompanyEmployeeSerializer(data=request.data)
        # check if the data is valid
        if serializer.is_valid():
            # save the new employee to the database
            # print(serializer)
            serializer.save()
            # return the serialized data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return an error if the data is not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)