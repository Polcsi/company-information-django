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
