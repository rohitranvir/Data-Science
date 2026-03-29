from django.contrib import admin
from testapp.models import student

# Register your models here.
class Studentadmin(admin.ModelAdmin):
    list_display = ['name','marks']
admin.site.register(student,Studentadmin)