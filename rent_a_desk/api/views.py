from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .filters import WorkspaceFilter
from .models import Reservation, Workspace
from .permissions import AdminOrReadOnly
from .serializers import ReservationSerializer, WorkspaceSerializer


class WorkspaceViewSet(viewsets.ModelViewSet):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer
    permission_classes = (AdminOrReadOnly,)
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
