from django.urls import path, include
from .views import *

urlpatterns = [
    path('books/', GetAllBooks.as_view()),
    path('books/<int:pk>', BooksRUD.as_view()),
    path('create_user/', UserRegister.as_view())
]
