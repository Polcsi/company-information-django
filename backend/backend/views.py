from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request):
    if request.method == 'GET':
        # get all drinks from the database
        drinks = Drink.objects.all()
        # serialize the drinks
        serializer = DrinkSerializer(drinks, many=True)
        # return the serialized data
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        # create a new drink from the request data
        serializer = DrinkSerializer(data=request.data)
        # check if the data is valid
        if serializer.is_valid():
            # save the new drink to the database
            serializer.save()
            # return the serialized data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return an error if the data is not valid
        return Response(serializer.errors, status=400)
    
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id):
    try:
        # get the drink from the database
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        # return a 404 if the drink does not exist
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        # serialize the drink
        serializer = DrinkSerializer(drink)
        # return the serialized data
        return Response(serializer.data)
    
    if request.method == 'PUT':
        # update the drink with the request data
        serializer = DrinkSerializer(drink, data=request.data)
        # check if the data is valid
        if serializer.is_valid():
            # save the updated drink to the database
            serializer.save()
            # return the serialized data
            return Response(serializer.data)
        # return an error if the data is not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        # delete the drink from the database
        drink.delete()
        # return a 204 response
        return Response(status=status.HTTP_204_NO_CONTENT)
