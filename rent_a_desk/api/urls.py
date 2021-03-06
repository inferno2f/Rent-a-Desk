from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import NewReservationAPIView, RerervationViewSet, WorkspaceViewSet

app_name = 'api'

router = SimpleRouter()
router.register(r'workspaces', WorkspaceViewSet)
router.register(r'reservations', RerervationViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/new_reservation/', NewReservationAPIView.as_view())
]
