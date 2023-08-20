from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SigningViewSet, clock_in, clock_out

router = DefaultRouter()
router.register(r'signings', SigningViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('clock-in/', clock_in, name='clock-in'),
    path('clock-out/', clock_out, name='clock-out'),
]
