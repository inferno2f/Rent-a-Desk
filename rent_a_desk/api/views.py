from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, permissions

from .filters import WorkspaceFilter
from .models import Reservation, Workspace
from .permissions import AdminOrReadOnly
from .serializers import ReservationSerializer, WorkspaceSerializer


class WorkspaceViewSet(viewsets.ModelViewSet):
    """
    View of all workspaces and their reservation times.
    Browsable by everyone, editable by admin.
    """
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filter_class = WorkspaceFilter
    pagination_class = None
    filterset_fields = (
        'reservations__booked_from',
        'reservations__booked_till',
    )


class NewReservationAPIView(generics.CreateAPIView):
    """
    Create new reservation view.
    Login required.
    Anonymous users can't make a reservation.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


class RerervationViewSet(viewsets.ModelViewSet):
    """
    View of all reservations. Available only to admin.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (permissions.IsAdminUser,)
