from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response

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

    def list(self, request, *args, **kwargs):
        from_date = self.request.query_params.get('reservations__booked_from')
        to_date = self.request.query_params.get('reservations__booked_till')
        if from_date and to_date:
            queryset = Workspace.objects.exclude(
                reservations__booked_from__range=(from_date, to_date)).exclude(
                reservations__booked_till__range=(from_date, to_date))
            serializer = WorkspaceSerializer(queryset, many=True)
            return Response(serializer.data)
        return super().list(request, *args, **kwargs)


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
