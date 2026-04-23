from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin
from django.db import models
class StudentManager(BaseUserManager):
    def create_user(self,email,username,phone_number,password=None):
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
class Student(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=150,unique=True)
    email= models.EmailField(unique=True)
    phone_number=models.CharField(max_length=15)
    college=models.CharField(max_length=200, blank=True)
    degree= models.CharField(max_length=100,blank=True)
    cgpa=models.FloatField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username','phone_number']
    objects = StudentManager()