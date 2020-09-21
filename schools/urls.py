from django.urls import path

from schools.views import SearchSchoolsView, SearchClassRoomsView

urlpatterns = [
    path('', SearchSchoolsView.as_view()),
    path('<school>/classrooms/', SearchClassRoomsView.as_view())
]
