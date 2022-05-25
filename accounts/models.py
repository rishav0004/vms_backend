from weakref import proxy
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from accounts.manager import UserManager


class CustomUser(AbstractUser):
    class Types(models.TextChoices):
        Head = 'Head','Head'
        Driver = 'Driver','Driver'
        Manager = 'Manager','Manager'
    # username = None
    type = models.CharField(_('Type'),choices=Types.choices,max_length=20,default=Types.Head)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(_('email address'), unique = True)
    dob = models.DateField(null=True)
    profile_image = models.ImageField(upload_to = 'images/')
    created_on = models.DateTimeField(auto_now_add=True)
    joined_on = models.DateField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    def __str__(self):
        return "{}".format(self.email) 
    

class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    vehicle_name = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    vehicle_year = models.CharField(max_length=20)
    type = [
        ('LTV','LTV'),
        ('HTV','HTV')
    ]
    vehicle_type = models.CharField(max_length=4,choices=type,default='LTV')
    vehicle_photo = models.ImageField(upload_to = 'images/')
    chassi_number = models.IntegerField()
    registration_number = models.CharField(max_length=40)

    def __str__(self):
        return self.vehicle_name

class DriverManager(models.Manager):
    
    def get_queryset(self,*args,**kwargs):
        return super().get_queryset(*args,**kwargs).filter(type=CustomUser.Types.Driver)

class HeadManager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        return super().get_queryset(*args,**kwargs).filter(type=CustomUser.Types.Head)

class ManagerManager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        return super().get_queryset(*args,**kwargs).filter(type=CustomUser.Types.Manager)


class Driver(CustomUser):
    driving_licence = models.ImageField(upload_to='images/')
    licence_expiry_date = models.DateField()
    vehicle_assigned = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    experience = models.IntegerField()
    objects = DriverManager()
    
    # def __str__(self):
    #     return self.user.first_name
    # class Meta:
    #     proxy = True
    class Meta:
        default_related_name = 'Driver'
    def save(self,*args,**kwargs):
        if not self.pk:
            self.type = CustomUser.Types.Driver
        return super().save(*args,**kwargs)

class Manager(CustomUser):
    # user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    objects = ManagerManager()
    # def __str__(self):
    #     return self.user.first_name
    class Meta:
        proxy = True
    def save(self,*args,**kwargs):
        if not self.pk:
            self.type = CustomUser.Types.Manager
        return super().save(*args,**kwargs)

        
class Head(CustomUser):
    # user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    objects = HeadManager()
    # def __str__(self):
    #     return self.user.first_name
    class Meta:
        proxy = True
    def save(self,*args,**kwargs):
        if not self.pk:
            self.type = CustomUser.Types.Head
        return super().save(*args,**kwargs)
 

# models.py
# ------------
# # Create Student Model
# class Student(models.Model):
#     admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
#     address = models.TextField()
#     gender = models.CharField(max_length=100)
#     course_id = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
#     session_year_id = models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.admin.first_name + " " + self.admin.last_nam




# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _

# from accounts.manager import UserManager

# # user_type = [
# #         ('Driver','Driver'),
# #         ('Manager','Manager'),
# #         ('Admin','Admin')
# #     ]


# class User(AbstractUser):
#     username = None
#     id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=40)
#     last_name = models.CharField(max_length=40)
#     email = models.EmailField(_('email address'), unique = True)
#     dob = models.DateField(null=True)
#     profile_image = models.ImageField(upload_to = 'images/')
#     is_driver = models.BooleanField(null=True)
#     is_admin = models.BooleanField(null=True)
#     is_manager = models.BooleanField(null=True)
#     # user_type = models.CharField(null=True,max_length=10,choices=user_type,default=None)
#     created_on = models.DateTimeField(auto_now_add=True)
#     joined_on = models.DateField(auto_now_add=True)
#     updated_on = models.DateTimeField(auto_now_add=True)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']
#     def __str__(self):
#         return "{}".format(self.email)
        
# class Vehicle(models.Model):
#     id = models.AutoField(primary_key=True)
#     vehicle_name = models.CharField(max_length=100)
#     vehicle_model = models.CharField(max_length=100)
#     vehicle_year = models.TextField()
#     type = [
#         ('LTV','LTV'),
#         ('HTV','HTV')
#     ]
#     vehicle_type = models.CharField(max_length=4,choices=type,default='LTV')
#     vehicle_photo = models.ImageField(upload_to = 'images/')
#     chassi_number = models.IntegerField()
#     registration_number = models.CharField(max_length=40)

#     def __str__(self):
#         return self.vehicle_name
    
    

# class Driver(User):
#     driving_licence = models.ImageField(upload_to='images/')
#     licence_expiry_date = models.DateField()
#     # is_driver = models.BooleanField(default=True)
#     vehicle_assigned = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
#     address = models.CharField(max_length=200)
#     experience = models.IntegerField()

#     class Meta:
#         default_related_name = 'Driver'

# class Manager(User):
#     username = None

#     def __str__(self):
#         return self.first_name

#     class Meta:
#         default_related_name = 'Manager'

# class Admin(User):
#     username = None
#     is_admin = True
    
#     def __str__(self):
#         return self.first_name

#     class Meta:
#         default_related_name = 'Admin'