from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import EventModel, Place, Ticket, UserModel
from rest_framework import viewsets
from .models import EventModel, Place, Ticket, UserModel
from .serializers import EventModelSerializer, PlaceSerializer, TicketSerializer, UserModelSerializer

class EventModelViewSet(viewsets.ModelViewSet):
    queryset = EventModel.objects.all()
    serializer_class = EventModelSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class UserModelViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer