from django.shortcuts import render,redirect
from django.views import View
from django.http import JsonResponse
from . models import *
from django.core.mail import EmailMessage
from django.contrib import auth
from django.contrib import messages

# Create your views here.
class DashboardView(View):
    def get(self,request):
        return render(request,'home/index.html')