from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import CharField


User = get_user_model()


class Workspace(models.Model):
    name = models.CharField('Workspace name', max_length=50, blank=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    workspace = models.ForeignKey(
        Workspace, on_delete=models.CASCADE, related_name='reservations')
    booked_from = models.DateTimeField('Start of the reservation')
    booked_till = models.DateTimeField('End of the reservation')
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
