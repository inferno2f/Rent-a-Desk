from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .filters import WorkspaceFilter
from .models import Workspace, Reservation
from .serializers import WorkspaceSerializer, ReservationSerializer


class WorkspaceViewSet(viewsets.ModelViewSet):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, )
    filter_class = WorkspaceFilter
    pagination_class = None
    filterset_fields = (
        'reservations__booked_from',
        'reservations__booked_till',
    )


class RerervationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
