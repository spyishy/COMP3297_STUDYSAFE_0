from django.urls import path, include
from .views import ViewVisitedVenues #, ViewCloseContacts

urlpatterns = [
    path('venues/<int:id>/<slug:date>/', ViewVisitedVenues.as_view(), name='display-visited-venues'),
    # path('contacts/<int:id>/<slug:date>/', ViewCloseContacts.as_view(), name='display-close-contacts'),
]
