import datetime
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Venue, HKUMember, Entry, Exit
from .serializers import VenueSerializer, HKUMemberSerializer, EntrySerializer, ExitSerializer

class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    lookup_field = 'venue_code'
    lookup_value_regex = '[^/]+'

    @action(detail=True, url_path='(?P<date>[^/]+)')
    def get_with_objectid(self, request, venue_code=None, date=None):
        queryset = Venue.objects.filter(exit__exit_hku_id__hku_id=venue_code).filter(exit__exit_date__range=[(datetime.datetime.strptime(date, "%Y-%m-%d") - datetime.timedelta(days=2)).strftime("%Y-%m-%d"), date]).only("venue_code")
        serializer = VenueSerializer(queryset, many=True)
        return Response([i["venue_code"] for i in serializer.data], status=status.HTTP_200_OK)

class HKUMemberViewSet(viewsets.ModelViewSet):
    queryset = HKUMember.objects.all()
    serializer_class = HKUMemberSerializer
    lookup_field = 'hku_id'
    lookup_value_regex = '[^/]+'

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

class ExitViewSet(viewsets.ModelViewSet):
    queryset = Exit.objects.all()
    serializer_class = ExitSerializer
