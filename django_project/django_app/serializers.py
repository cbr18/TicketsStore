from rest_framework import serializers
from .models import EventModel, Place, Ticket, UserModel, TicketCategory


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__' 

class EventModelSerializer(serializers.ModelSerializer):
    place = PlaceSerializer(read_only=True)

    class Meta:
        model = EventModel
        fields = '__all__'

class TicketCategorySerializer(serializers.ModelSerializer):
    eventTo = EventModelSerializer(read_only=True)

    class Meta:
        model = TicketCategory
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    categoryTo = TicketCategorySerializer(read_only=True)
    userTo = serializers.PrimaryKeyRelatedField(read_only=True) 

    class Meta:
        model = Ticket
        fields = '__all__'

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'firebase_id', 'registerDate')