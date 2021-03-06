"""dj_exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from exam_assign import views as exam_assign_views
from exams import views as exams_views
from home import views as home_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path("signup/", accounts_views.signup, name="signup"),
    path("", home_views.my_exam_list, name="home"),
    path("enroll_exam/<int:id>", exam_assign_views.enroll_exam, name="enroll_exam"),
    path("start_exam/<int:id>", exam_assign_views.start_exam, name="start_exam"),
    path("submit_exam/<int:id>", exam_assign_views.submit_exam, name="submit_exam"),
    path("exam_result/<int:id>", home_views.exam_result, name="exam_result"),
]
