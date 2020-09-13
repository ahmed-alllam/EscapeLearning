from django.urls import path

from students import views

urlpatterns = [
    path('/register/', views.RegisterStudentView()),
    path('/me/', views.ManageStudentView()),
]