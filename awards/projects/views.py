from django.shortcuts import render,redirect
from django.views import View
from django.http import JsonResponse
from . models import *
from django.core.mail import EmailMessage
from django.contrib import auth
from django.contrib import messages
import json
from django.http import JsonResponse
# Create your views here.
class DashboardView(View):
    def get(self,request):
        projects = Project.objects.all()
        return render(request,'home/index.html',{"projects":projects})
class LoginView(View):
    def get(self,request):
        return render(request,'authentication/login.html')
    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']
        if email and password:
            user = auth.authenticate(email=email,password=password)
            if user:
                auth.login(request,user)
                return redirect('/')
            else:
                messages.error(request,'Invalid login')
                return render(request,'authentication/login.html')
        messages.error(request,'Invalid login credentials')
        return render(request,'authentication/login.html')
class LogoutView(View):
    def post(self,request):
        auth.logout(request)
        messages.success(request,"You have successfully logged out")
        return redirect('/')
####REGISTER VIEW
class RegisterView(View):
    def get(self,request):
        return render(request,'authentication/register.html')
    def post(self,request):
        username = request.POST['username']
        email = request.POST['email']
        full_name = request.POST['full_name']
        password = request.POST['password']
        bio = request.POST['bio']
        if not Profile.objects.filter(username=username).exists():
            if not Profile.objects.filter(email=email).exists():
                profile = Profile.objects.create_user(username=username,email=email,password=password,full_name=full_name,bio=bio)
                # profile.set_password(password)
                profile.save()
                email = EmailMessage(
                    'Awards Account',
                    'Awards account created successfully',
                    'liznabuuso@gmail.com',
                    [email]
                )
                email.send(fail_silently=True)
                return JsonResponse({"message":"Account created successfully","status":201},status=201)
            else:
                return JsonResponse({"error":"Username already taken","status":400},status=400)
        else:
            return JsonResponse({"error":"Email already taken","status":400},status=400)
##PROJECTS
class ProjectsView(View):
    def post(self,request):
        img = request.FILES.get("image")
        name = request.POST['name']
        description = request.POST['description']
        profile = request.POST['profile']
        link = request.POST['link']
        # fss = FileSystemStorage()
        # filename = fss.save(img.name,img)
        # url = fss.url(filename)
        project = Project()
        project.image = img
        project.name = name
        project.description = description
        p = Profile.objects.get(pk=profile)
        project.profile = p
        project.link = link
        project.save_image()
        # Image.save_image(image=url,image_name=image_name,image_caption=image_caption,profile=profile)
        return JsonResponse({"success":"Image uploaded successfully","status":201},status=201)
class RatingView(View):
    def post(self,request):
        design = request.POST['design']
        usability = request.POST['usability']
        content = request.POST['content']
        project = request.POST['project']
        profile = request.POST['profile']
        rating = Rating(design_rating=design,usability_rating=usability,content_rating=content,project_id=project,profile_id=profile)
        rating.save()
        return JsonResponse({"message":"Rated successfully","status":201},status=201)
##USERS
class ProfilesView(View):
    def get(self,request):
        projects = Project.objects.filter(profile=request.user)
        return render(request,'home/profile.html',{"projects":projects})
###SEARCH PROJECTS
class SearchProject(View):
    def post(self,request):
        search_str = json.loads(request.body).get('searchText')
        projects = Project.filter(name__icontains=search_str) | Project.filter(design_rating__icontains=search_str) | Project.filter(usability_rating__icontains=search_str) | Project.filter(profile__full_name__icontains=search_str) 
        data = projects.values()
        return JsonResponse(list(data),safe=False)
