from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('password/reset/confirm/<str:uid>/<str:token>/',views.passwordResetConfirm,name='reset'),
    path('activate/<str:uid>/<str:token>/',views.userActivation,name='activate'),
    path('resend_activatation/',views.userReActivation,name='resend_activation')

]







