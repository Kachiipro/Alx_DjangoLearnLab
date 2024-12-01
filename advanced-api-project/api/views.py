from django.shortcuts import render
from rest_framework import generics
from .models import Book #replace with your working model
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.




class CustomBookCreateView(generics.CreateAPIView):
# can be any name, ensure to align with your project as this is sample exampls 
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class CustomBookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =[IsAuthenticated]

class CustomBookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    permission_classes = [IsAuthenticated]


class CustomBookUpdateView(generics.UpdateAPIView):
     queryset = Book.objects.all()
     serializer_class = BookSerializer
     permission_classes = [IsAuthenticated]
class CustomBookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


