from django.contrib import admin

from .models import Reservation, Workspace

admin.site.register(Workspace)
admin.site.register(Reservation)
