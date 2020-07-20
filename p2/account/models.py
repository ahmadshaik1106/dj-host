# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# class UserAccountManager(BaseUserManager):
#     def create_user(self,username,email,password=None):
#         if not email:
#             return ValueError('This field is required')
#         if not username:
#             return ValueError('This field is required')
        

#         user = self.model(username=username.upper(),email=self.normalize_email(email))
#         user.set_password(password)
#         user.save()

#         return user
    
#     def create_superuser(self,username,email,password):
#         user = self.model(
#             email    = self.normalize_email(email),
#             username = username.upper(),
#             password = password, 
#         )
#         user.is_staff     = True 
#         user.is_superuser = True
#         user.is_admin     = True
        
#         user.set_password(password)
#         user.save()
#         return user
    
# class UserAccount(AbstractBaseUser,PermissionsMixin):
#     username      = models.CharField(verbose_name='Roll no.',max_length=10,unique=True)
#     email         = models.EmailField(max_length=150,unique=True)
#     date_joined   = models.DateTimeField(verbose_name='date joined',auto_now_add=True)
#     last_login    = models.DateTimeField(verbose_name='last login',auto_now=True)
#     is_active     = models.BooleanField(default=True)
#     is_staff      = models.BooleanField(default=False)
#     is_superuser  = models.BooleanField(default=False)
#     is_admin      = models.BooleanField(default=False)
     

#     objects = UserAccountManager()

#     USERNAME_FIELD  = 'username'
#     REQUIRED_FIELDS = ['email']

#     def get_email(self):
#         return self.email
#     def get_username(self):
#         return self.username
    
#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def __str__(self):
#         return self.username

    