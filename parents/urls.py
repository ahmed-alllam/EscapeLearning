from django.urls import path

from parents import views

urlpatterns = [
    path('/register/', views.RegisterParentView()),
    path('/me/', views.ManageParentView()),
]
