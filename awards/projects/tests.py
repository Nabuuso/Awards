from django.test import TestCase
from projects.models import *

# Create your tests here.
class TestUser(TestCase):
    def test_should_create_profile(self):
        profile = Profile.objects.create_user(full_name='full name',email='email@app.com',username='username',bio='bio',password='password')
        profile.save()
        self.assertEqual(str(profile), 'full name')
##TEST PROJECTS
class TestProjects(TestCase):
    def test_create_project(self):
        profile = Profile.objects.create_user(full_name='full name',email='email@app.com',username='username',bio='bio',password='password')
        profile.save()

        project = Project(name='name',description='description',profile=profile,link='link',design_rating=0,usability_rating=0,content_rating=0,total_raters=0)
        project.save()

        self.assertEqual(str(project), 'name')