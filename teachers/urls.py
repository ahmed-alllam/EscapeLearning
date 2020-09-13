from django.urls import path

from teachers import views

urlpatterns = [
    path('/register/', views.RegisterTeacherView()),
    path('/me/', views.ManageTeacherView()),
]
