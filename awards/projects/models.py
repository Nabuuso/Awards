from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
import os

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,full_name,username,email,password,*args,**kwargs):
        if email is None:
            raise TypeError("Email field cannot be null")
        user = self.model(full_name=full_name,username=username,email=email,*args,**kwargs)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,password,*args,**kwargs):
        user = self.model(**kwargs)
        user.set_password(password)
        user.save()
        return user

class Profile(AbstractBaseUser,PermissionsMixin):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True)
    username = models.CharField(max_length=255,unique=True)
    bio = models.TextField(null=True)
    profile_photo = models.ImageField(upload_to="images/profile",null=True)
    password = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name','username','password']
    objects = UserManager()

    def __str__(self):
        return self.full_name
    class Meta:
        ordering = ['-created_date']
class Project(models.Model):
    image = models.ImageField(upload_to="images/project",null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="profile_projects")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    design_rating = models.IntegerField(default=0)
    usability_rating = models.IntegerField(default=0)
    content_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.image_name
    def save_image(self,*args,**kwargs):
        super().save(*args,**kwargs)
    def delete_image(self,pk):
        img = Project.objects.get(pk=pk)
        if len(img.image) > 0:
            os.remove(img.image.path)
        img.delete()
    def update_caption(self,*args,**kwargs):
        super().update(*args,**kwargs)
    
    class Meta:
        ordering = ['-created_date']
class Rating(models.Model):
    design_rating = models.IntegerField(default=0)
    usability_rating = models.IntegerField(default=0)
    content_rating = models.IntegerField(default=0)
    project = models.ForeignKey(Project,on_delete=models.DO_NOTHING)
    profile = models.ForeignKey(Profile,on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_date']
