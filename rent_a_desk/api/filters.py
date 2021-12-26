from django_filters import FilterSet
from django_filters.filters import DateTimeFilter

from .models import Workspace


class WorkspaceFilter(FilterSet):
    reservations__booked_from = DateTimeFilter(exclude=True)
    reservations__booked_till = DateTimeFilter(exclude=True)

    class Meta:
        model = Workspace
        fields = ('reservations__booked_from', 'reservations__booked_till')
