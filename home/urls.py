from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('user_profile', views.profile, name='profile'),
    path('upload_pic', views.uploadPic, name = 'upload_pic'),
    path('addName', views.addName, name='addName'),

]
