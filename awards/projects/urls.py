from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('',DashboardView.as_view(),name='dashboard'),
    path('register',csrf_exempt(RegisterView.as_view()),name="register"),
    path('login',LoginView.as_view(),name="login"),
    path('logout',LogoutView.as_view(),name='logout'),
    path('project-list',csrf_exempt(ProjectsView.as_view()),name='project-list'),
    path('profile-view',ProfilesView.as_view(),name="profile-view"),
    path('rating',csrf_exempt(RatingView.as_view()),name='rating'),
    path('profiles',ProfileAPIView.as_view(),name="profiles"),
    path('projects',ProjectsAPIView.as_view(),name="projects")
]