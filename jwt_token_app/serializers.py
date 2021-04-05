from rest_framework import serializers
from .models import School, Library

class SchoolSerializers(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['lib']=LibrarySerializers(instance.lib).data
        return response

class LibrarySerializers(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'

