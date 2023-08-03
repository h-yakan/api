from django.shortcuts import render
from rest_framework import status
from bookApi.models import Book
from bookApi.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
# @api_view(['GET'])
# def bookList(req):
#     books = Book.objects.all()
#     serialized = BookSerializer(books,many=True)
#     return Response(serialized.data)
    
# @api_view(['POST'])
# def bookCreate(req):
#     serializer = BookSerializer(data=req.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)

@api_view(['GET','POST'])
def books(req):
    if req.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)
    if req.method == "POST":
        serializer = BookSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors)

# @api_view(['GET'])
# def book(req,id):
    
    
# @api_view(['PUT'])
# def bookUpdate(req,id):
    
    
@api_view(['GET','PUT','DELETE'])
def bookById(req,id):
    if req.method == "GET":
        try:
            books = Book.objects.get(pk=id)
            serializer = BookSerializer(books)
            return Response(serializer.data)
        except:
            return Response({"Error":"Eşleşen bir kayıt bulunamadı"},status=status.HTTP_404_NOT_FOUND)
    if req.method == "PUT":
        book = Book.objects.get(pk = id)
        serializer = BookSerializer(book,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    if req.method =="DELETE":
        book = Book.objects.get(pk=id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
