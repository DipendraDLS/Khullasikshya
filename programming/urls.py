from django.urls import path
from programming import views

urlpatterns = [

    ############################ Backend Urls #######################################
    path('programming/', views.programming, name='programming'),
    path('add_programming', views.addProgrammingLanguage, name='add_programming_language'),
    path('programDelete/<int:program_id>/', views.adminProgramDelete, name='programDelete'),
    path('programEdit/<int:program_id>/', views.adminProgramEdit, name='programEdit'),

    ################################## Frontend Urls ###############################
    path('programmingHomePage', views.programmingHomePage, name='programmingHomePage'),
    path('programmingDetails/<int:program_id>', views.programmingDetails, name='programmingDetails'),

]
