from django.contrib import admin

# Register your models here.
from testapp.models import HydJobs,Bangjobs,Punejobs
class HydjobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(HydJobs,HydjobsAdmin)

class BangjobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(Bangjobs,BangjobsAdmin)

class PunejobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(Punejobs,PunejobsAdmin)