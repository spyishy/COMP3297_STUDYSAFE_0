from rest_framework import serializers
from .models import Venue, HKUMember, Entry, Exit

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'
        lookup_field = 'venue_code'

class HKUMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = HKUMember
        fields = '__all__'
        lookup_field = 'hku_id'

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'

class ExitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exit
        fields = '__all__'
