from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import WorkspaceViewSet, RerervationViewSet

app_name = 'api'


router = SimpleRouter()
router.register(r'workspaces', WorkspaceViewSet)
router.register(r'reservations', RerervationViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
