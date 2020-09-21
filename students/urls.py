from django.urls import path

from students import views

urlpatterns = [
    path('register/', views.RegisterStudentView().as_view()),
    path('me/', views.ManageStudentView().as_view()),
]
