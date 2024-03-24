from django.db import models
from django.contrib.auth.models import User

class EventModel (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    place = models.ForeignKey('Place', on_delete=models.PROTECT, null=True)
    date = models.DateField()
    minAge = models.IntegerField(default=0)
    description = models.TextField(null = True)

    def __str__(self):
        return self.name

class Place (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    capacity_standing = models.IntegerField(default = 0)
    capacity_seats = models.IntegerField(default = 0)

    def __str__(self):
        return self.name
    

class TicketCategory (models.Model):
    id = models.IntegerField(primary_key=True)
    eventTo = models.ForeignKey('EventModel', on_delete=models.PROTECT, null=True)
    price = models.IntegerField(default = 0)
    category = models.CharField(max_length=30)
    entryTime = models.DateTimeField()

    def __str__(self):
        return self.name

class Ticket (models.Model):
    id = models.IntegerField(primary_key=True)
    categoryTo = models.ForeignKey('TicketCategory', on_delete=models.PROTECT, null=True)
    userTo = models.ForeignKey('UserModel', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name
    
class UserModel (User):
    firebase_id = models.CharField(max_length=30)
    registerDate = models.DateField(null = True)

    def __str__(self):
        return self.username