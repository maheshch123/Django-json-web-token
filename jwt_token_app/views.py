from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .serializers import SchoolSerializers,LibrarySerializers
from .models import School,Library
from rest_framework import viewsets
# Create your views here.

class SchoolApi(viewsets.ModelViewSet):
    serializer_class = SchoolSerializers
    queryset = School.objects.all()
    permission_classes = (IsAuthenticated,)
    

class libraryApi(viewsets.ModelViewSet):
    serializer_class = LibrarySerializers
    queryset = Library.objects.all()
    permission_classes = (IsAuthenticated,)

