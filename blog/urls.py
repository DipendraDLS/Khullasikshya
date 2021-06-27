from django.urls import path
from blog import views


urlpatterns = [
    path('blog/',views.blog, name='blog'),
    path('adminBlog/', views.adminBlog, name='adminBlog'),
    path('delete/<int:id>/',views.adminBlogDelete,name='delete'),
    path('edit/<int:id>/', views.adminBlogEdit, name='edit'),
    path('blogDetail/<int:id>/',views.blogDetail,name='blogDetail'),
    path('blogComment', views.blogComment, name='blogComment')
     
]