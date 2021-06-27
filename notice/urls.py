from django.urls import path
from . import views

urlpatterns =[
    path('notice/',views.notice, name='notice'),
    path('adminNotice/', views.adminNotice, name='adminNotice'),
    path('noticeDelete/<int:id>/',views.adminNoticeDelete,name='noticeDelete'),
    path('noticeEdit/<int:id>/', views.adminNoticeEdit, name='noticeEdit'),

]