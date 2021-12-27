from django_filters import FilterSet
from django_filters.filters import DateTimeFilter

from api.models import Workspace


class WorkspaceFilter(FilterSet):
    reservations__booked_from = DateTimeFilter()
    reservations__booked_till = DateTimeFilter()

    class Meta:
        model = Workspace
        fields = ('reservations__booked_from', 'reservations__booked_till')
