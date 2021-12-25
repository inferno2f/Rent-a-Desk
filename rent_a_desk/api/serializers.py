from django.db.models.fields import DateField, DateTimeCheckMixin
from rest_framework import serializers
from rest_framework.fields import DateTimeField

from .models import Workspace, Reservation


class WorkspaceSerializer(serializers.ModelSerializer):
    reservations = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Workspace
        fields = ('id', 'name', 'reservations')


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
