from django.urls import path
from . import views

urlpatterns = [


    path('adminHome/', views.adminHome, name="adminHome"),
    path('userList/', views.userShow, name="userShow"),

    path('userDelete/<int:id>', views.userDelete, name="userDelete"),

    path('userEdit/<int:id>', views.userEdit, name="userEdit"),
    path('search/', views.search, name="search")
]