# from django.views.generic import TemplateView
# from .models import Venue, HKUMember, Entry, Exit

# class ViewVisitedVenues(TemplateView):
#     template_name = "venues.html"
#     def get_context_data(self, **kwargs):
#         subject = self.kwargs['id']
#         date = self.kwargs['date']
#         context = super().get_context_data(**kwargs)
#         context['subject'] = subject # to be refined
#         context['date'] = date # to be refined
#         context['venues'] = Venue.objects.all # to be modified
#         return context

# class ViewCloseContacts(TemplateView):
#     template_name = "contacts.html"
#     def get_context_data(self, **kwargs):
#         subject = self.kwargs['id']
#         date = self.kwargs['date']
#         context = super().get_context_data(**kwargs)
#         context['subject'] = subject # to be refined
#         context['date'] = date # to be refined
#         context['contacts'] = HKUMember.objects.all # to be modified
#         return context
