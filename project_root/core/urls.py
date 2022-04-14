from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import VenueViewSet, HKUMemberViewSet, EntryViewSet, ExitViewSet
#from .views import ViewVisitedVenues, ViewCloseContacts

router = DefaultRouter()
router.register(r'venues', VenueViewSet, 'venue')
router.register(r'hku-members', HKUMemberViewSet, 'member')
router.register(r'entries', EntryViewSet, 'entries')
router.register(r'exits', ExitViewSet, 'exits')

urlpatterns = [
    path('api/', include(router.urls)),
    # path('venues/<int:id>/<slug:date>', ViewVisitedVenues.as_view(), name='display-visited-venues'),
    # path('contacts/<int:id>/<slug:date>', ViewCloseContacts.as_view(), name='display-close-contacts'),
]
