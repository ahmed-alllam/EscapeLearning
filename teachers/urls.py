from django.urls import path

from teachers import views

urlpatterns = [
    path('register/', views.RegisterTeacherView().as_view()),
    path('me/', views.ManageTeacherView().as_view()),
]
