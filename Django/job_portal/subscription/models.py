from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from datetime import timedelta
from users.models import Student
class Subscription(models.Model):
    STATUS=[('pending','Pending'),('active','Active'),('expired','Expired')]
    student=models.OneToOneField(Student,on_delete=models.CASCADE)
    status=models.CharField(max_length=10,choices=STATUS,default='pending')
    amount=models.DecimalField(max_digits=8,decimal_places=2,default=499.0)
    start_date=models.DateField(null=True,blank=True)
    end_date=models.DateField(null=True,blank=True)
    def activate(self):
        self.status='active'
        self.start_date=timezone.now()
        self.end_date=timezone.now()+timedelta(days=30)
        self.save()
    def is_active(self):
        return self.status=='active' and self.end_date and timezone.now()<self.end_date