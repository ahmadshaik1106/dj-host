from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
import uuid


class UserManager(BaseUserManager):

    def create_user(self,username,email,password=None):

        if username is None:
            raise TypeError('user should have username')

        if email is None:
            raise TypeError('user should have email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user


    def create_superuser(self,username,email,password=None):

        if username is None:
            raise TypeError('user should not be empty')

        user = self.create_user(username, email,password)
        user.is_superuser = True
        user.is_staff = True
        user.is_verified = True
        user.save()

        return user

class User(AbstractBaseUser,PermissionsMixin):

    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    username = models.CharField(max_length=225,unique=True,db_index=True)
    email = models.EmailField(max_length=225,unique=True,db_index=True)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username

    def tokens(self):
        return ''


