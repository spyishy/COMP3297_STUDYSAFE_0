import requests
from django.views.generic import TemplateView

class ViewVisitedVenues(TemplateView):
    template_name = "venues.html"
    
    def get_context_data(self, **kwargs):
        id = self.kwargs['id']
        date = self.kwargs['date']

        response = requests.get("https://studysafe-b-group-e.herokuapp.com/api/entries/" + str(id) + "/" + date + "/")
        if response.status_code == 200:
            venues = response.json()
        else:
            venues = requests.get("http://127.0.0.1:8000/api/entries/" + str(id) + "/" + date + "/").json()
        venues = sorted(list(set(venues)))

        context = super().get_context_data(**kwargs)
        context['subject'] = str(id)
        context['date'] = date
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
