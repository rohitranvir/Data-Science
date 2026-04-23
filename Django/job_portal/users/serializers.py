from rest_framework import serializers
from .models import Student
class RegisterSerializer(serializers.ModelSerialzer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=Student
        fields=['username','email','phone_number','password']
    def create(self,validated_data):
        return Student.objects.create_user(**validated_data)
class ProfileSerializer(serializers.ModelSerialzer):
    class Meta:
        model=Student
        fields=['id','username','email','phone_number','college','degree','cgpa']