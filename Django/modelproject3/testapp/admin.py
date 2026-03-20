from django.contrib import admin
from django.contrib.admin import ModelAdmin
from testapp.models import Student


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['rollno','name','dob','marks','email','phonenumber']
admin.site.register(Student,StudentAdmin)