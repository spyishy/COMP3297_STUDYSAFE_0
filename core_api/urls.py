from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import VenueViewSet, HKUMemberViewSet, EntryViewSet, ExitViewSet

router = DefaultRouter()
router.register(r'venues', VenueViewSet, 'venue')
router.register(r'hku-members', HKUMemberViewSet, 'member')
router.register(r'entries', EntryViewSet, 'entries')
router.register(r'exits', ExitViewSet, 'exits')

urlpatterns = [
    path('', include(router.urls)),
]
