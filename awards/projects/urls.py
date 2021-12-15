from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('',DashboardView.as_view(),name='dashboard'),
    path('register',csrf_exempt(RegisterView.as_view()),name="register"),
    path('login',LoginView.as_view(),name="login"),
    path('logout',LogoutView.as_view(),name='logout'),
    path('projects',csrf_exempt(ProjectsView.as_view()),name='projects')
]