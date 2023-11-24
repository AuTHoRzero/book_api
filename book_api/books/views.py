from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets, mixins

# Create your views here.

class GetAllBooks(APIView):

    def get(self, request, *args, **kwargs):
        '''
        Get all Book
        '''
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        '''
        Create new book
        '''
        data = {
            'name': request.data.get('name'), 
            'author': request.data.get('author'), 
            'publicate_date': request.data.get('publicate_date'),
            'isbn': request.data.get('isbn')
        }
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BooksRUD(APIView):

    def get_object(self, pk):
        '''
        Search object
        '''
        try:
            return Book.objects.get(id=pk)
        except Book.DoesNotExist:
            return None
    
    def get(self, request, pk, *args, **kwargs):
        '''
        Detail Book obj
        '''
        book_instance = self.get_object(pk)
        if not book_instance:
            return Response(
                {"res": "Object not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BookSerializer(book_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        '''
        Update Book
        '''
        book_instance = self.get_object(pk)

        #Commit comment
        if not book_instance:
            return Response(
                {"res": "Object not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'), 
            'author': request.data.get('author'), 
            'publicate_date': request.data.get('publicate_date'),
            'isbn': request.data.get('isbn')
        }
        serializer = BookSerializer(instance = book_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        '''
        Deletes Book
        '''
        book_instance = self.get_object(pk)
        if not book_instance:
            return Response(
                {"res": "Object not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        book_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class UserRegister(APIView):
    
    def post(self, request, *args, **kwargs):
        '''
        Create user
        '''
        data = {
            'username': request.data.get('username'), 
            'email': request.data.get('email'), 
            'password': request.data.get('password')
        }
        serializer = CreateUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)