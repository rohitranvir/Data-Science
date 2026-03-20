from django.contrib import admin

# Register your models here.
from testapp.models import temp
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eaddr']
admin.site.register(temp,EmployeeAdmin)