from rest_framework.generics import ListAPIView

from schools.models import School, ClassRoom
from schools.serializers import SchoolSerializer, ClassRoomSerializer


class SearchSchoolsView(ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def filter_queryset(self, queryset):
        return self.get_queryset().filter(name__icontains=self.request.query_params.get('search', ''))


class SearchClassRoomsView(ListAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer

    def filter_queryset(self, queryset):
        return self.get_queryset().filter(school__name__iexact=self.kwargs.get('school', ''))
