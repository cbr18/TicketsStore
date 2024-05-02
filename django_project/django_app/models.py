from django.db import models
from django.contrib.auth.models import AbstractUser

class EventModel (models.Model):
    id = models.IntegerField(primary_key=True , auto_created=True)
    name = models.CharField(max_length=30)
    place = models.ForeignKey('Place', on_delete=models.PROTECT, null=True)
    date = models.DateField()
    minAge = models.IntegerField(default=0)
    description = models.TextField(null = True)

    def __str__(self):
        return self.name

class Place (models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    capacity_standing = models.IntegerField(default = 0)
    capacity_seats = models.IntegerField(default = 0)

    def __str__(self):
        return self.name
    

class TicketCategory (models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    eventTo = models.ForeignKey('EventModel', on_delete=models.PROTECT, null=True)
    price = models.IntegerField(default = 0)
    category = models.CharField(max_length=30)
    entryTime = models.DateTimeField()

    def __str__(self):
        return self.name

class Ticket (models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    categoryTo = models.ForeignKey('TicketCategory', on_delete=models.PROTECT, null=True)
    userTo = models.ForeignKey('User', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name
    
class User (AbstractUser):
    email = models.CharField(max_length=256, unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)    
    username = models.CharField(max_length=256, unique=True)
    REQUIRED_FIELDS = ['email']
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.email

