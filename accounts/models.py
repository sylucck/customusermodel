import email
from turtle import update
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

#3
class UserManager(BaseUserManager):
    #creating a user
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):

        if not email:
            raise ValueError("Users must have an email address")
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password) #can change user password with this pattern.
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True,

        )
        return user

    


#user class- customized. #1
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    #full_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    #confirmed_email = models.BooleanField(default=False)


    USERNAME_FIELD = 'email' #username is now set to 'email'
    

    #USERNAME_FIELD and password are required by default. Hence, [].
    REQUIRED_FIELDS = [] #['full_name']

    objects = UserManager() #2

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_superuser(self):
        return self.admin

#class Profile(models.Model):
#   user = models.OneToOneField(User)




class GuestEmail(models.Model):
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timetsamp = models.DateTimeField(auto_now=True)


    def __init__(self):
        return self.email