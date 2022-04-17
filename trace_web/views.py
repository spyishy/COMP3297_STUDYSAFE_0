import requests
from django.views.generic import TemplateView

class ViewVisitedVenues(TemplateView):
    template_name = "venues.html"
    def get_context_data(self, **kwargs):
        subject = self.kwargs['id']
        date = self.kwargs['date']

        # temporarily retrieve all venues as visited venues
        response = requests.get("http://127.0.0.1:8000/api/venues/").json()
        venues = []
        for venue in response:
            venues.append(venue['venue_code'])
        venues = sorted(venues)

        context = super().get_context_data(**kwargs)
        context['subject'] = subject # to be refined
        context['date'] = date # to be refined
        context['venues'] = venues
        return context

class ViewCloseContacts(TemplateView):
    template_name = "contacts.html"
    def get_context_data(self, **kwargs):
        subject = self.kwargs['id']
        date = self.kwargs['date']

        # temporarily retrieve all hku members as close contacts
        response = requests.get("http://127.0.0.1:8000/api/hku-members/").json()
        members_ = {}
        for member in response:
            hku_id = member['hku_id']
            name = member['name']
            members_[hku_id] = name
        ids = sorted(members_.keys())
        members = []
        for id in ids:
            members.append(str(id + " (" + members_[id]) + ")")

        context = super().get_context_data(**kwargs)
        context['subject'] = subject # to be refined
        context['date'] = date # to be refined
        context['contacts'] = members
        return context
