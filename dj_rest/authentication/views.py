from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from rest_framework import generics, status
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer

from .models import User
from .Utils import Util


class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer

    def  post(self,request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request)
        relativeLink = reverse('verify-email')

        absurl = f'http://{current_site}{relativeLink}?={str(token)}'

        subject = 'Verify your email'
        body = f'Hi {user.username} \nverify your email by clicking the following link \n{absurl}'
        to_email = user.email
        data = {'subject':subject,'body':body,'to_email':to_email}

        Util.send_email(data)

        return Response(user_data,status=status.HTTP_201_CREATED)
    
    
class VerifyEmail(generics.GenericAPIView):
    def get(self):
        pass
