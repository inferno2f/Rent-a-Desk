import datetime as dt

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q
from django.db.models.constraints import CheckConstraint

User = get_user_model()


class Workspace(models.Model):
    name = models.CharField('Workspace name', max_length=50, blank=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    workspace = models.ForeignKey(
        Workspace, on_delete=models.CASCADE, related_name='reservations')
    created_on = models.DateTimeField('Date of creation', auto_now_add=True)
    booked_from = models.DateTimeField('From:', blank=False)
    booked_till = models.DateTimeField('Until:', blank=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(booked_from__gte=dt.datetime.now()),
                name='valid_booking_time'), ]

    def __str__(self) -> str:
        booking_info = (f'Reservation id:{self.id} | '
                        f'Customer: {self.customer} | '
                        f'Date: {self.booked_from}')
        return booking_info
