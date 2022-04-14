from rest_framework import viewsets
from .models import Venue, HKUMember, Entry, Exit
from .serializers import VenueSerializer, HKUMemberSerializer, EntrySerializer, ExitSerializer

class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    lookup_field = 'venue_code'
    lookup_value_regex = '[^/]+'

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
