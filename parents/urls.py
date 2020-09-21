from django.urls import path

from parents import views

urlpatterns = [
    path('register/', views.RegisterParentView().as_view()),
    path('me/', views.ManageParentView().as_view()),
]
