from rest_framework import serializers

from .models import Reservation, Workspace


class WorkspaceSerializer(serializers.ModelSerializer):
    reservations = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Workspace
        fields = ('id', 'name', 'reservations')


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('workspace', 'booked_from', 'booked_till')
