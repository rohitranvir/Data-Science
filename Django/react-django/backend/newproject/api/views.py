from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializer import BookSerializers

@api_view(['GET'])
def get_books(request):
    books=Book.objects.all()
    serializedData=BookSerializers(books,many=True).data
    return Response(serializedData)

@api_view(['POST'])
def create_books(request):
    data=request.data
    serializer=BookSerializers(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE'])
def book_details(request,id):
    try:
        book=Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method=='PUT':
        data=request.data
        serializer=BookSerializers(book,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




