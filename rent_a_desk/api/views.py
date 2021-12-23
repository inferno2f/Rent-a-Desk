from django.shortcuts import render
from rest_framework import viewsets

from .models import Workspace


class WorkspaceViewSet(viewsets.ModelViewSet):
    queryset = Workspace.objects.all()
