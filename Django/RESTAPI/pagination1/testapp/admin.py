from django.contrib import admin
from testapp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','addr']
admin.site.register(Employee,EmployeeAdmin)
