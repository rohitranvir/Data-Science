from django.contrib import admin

# Register your models here.
from testapp.models import HydJobs
class HydjobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(HydJobs,HydjobsAdmin)