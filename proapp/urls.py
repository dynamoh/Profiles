"""Profile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from .views import AboutPage,UserList,UserDetail,signup,UserCreate,UserUpdateView,UserDeleteView,LogoutPage
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',UserList.as_view(),name="userslist"),
    path('about/',AboutPage.as_view(),name="aboutpage"),
    path('detail/<str:slug>/',UserDetail.as_view(),name="usersdetail"),
    path('create/',UserCreate.as_view(),name="usercreate"),
    path('update/<str:slug>/',UserUpdateView.as_view(),name="userupdate"),
    path('delete/<str:slug>/',UserDeleteView.as_view(),name="userdelete"),
    path('signup/',signup,name="signuppage"),
    path('lgout/',LogoutPage.as_view(),name="lgpage"),
    path('accounts/login/',LoginView.as_view(template_name='registration/login.html/'),name="loginpage"),
    path('accounts/logout/',LogoutView.as_view(template_name='registration/logout.html/'),name='logoutpage',kwargs={'next_page':'home'}),


]
