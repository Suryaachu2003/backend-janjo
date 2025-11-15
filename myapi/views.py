from django.urls import render


from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *



@api_view(['GET'])

def senddata(request):
    table=Product.objects.all()
    serializer=ProductSerializer(table,many=True)
    return Response(serializer.data)

@api_view(['post'])

def getdata(request):
    # serializer=ProductSerializer(data=request.data)
    is_many = isinstance(request.data, list)
    serializer = ProductSerializer(data=request.data, many=is_many)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)