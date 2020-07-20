from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect

from rest_framework.response import Response
from django.contrib import messages
from rest_framework.decorators import api_view 
import requests

def passwordResetConfirm(request,uid,token):
    context = {'token':token,'uid':uid}
    return render(request,"account/reset_password_confirm.html",context)

def userActivation(request,uid,token):
    context = {'token':token,'uid':uid}
    return render(request,"account/activate_user.html",context)

def userReActivation(request):
    context = {}
    return render(request,"account/reactivate_user.html",context)
