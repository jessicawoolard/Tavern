from django.urls import reverse
from .models import Lunch
from .models import Location
from django.views.generic import TemplateView, View
from django.http import HttpResponseRedirect


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        lunches = Lunch.objects.all()

        context = {
            'lunches': lunches

        }
        return context


class DetailView(TemplateView):
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        lunch_pk = self.kwargs.get('pk')
        lunch = Lunch.objects.get(pk=lunch_pk)
        locations = Location.objects.filter(lunch__pk=lunch_pk)

        context = {
            'locations': locations,
            'lunch': lunch
        }
        return context


class ResultsView(TemplateView):
    template_name = 'results.html'

    def get_context_data(self, **kwargs):
        lunch_pk = self.kwargs.get('pk')
        lunch = Lunch.objects.get(pk=lunch_pk)
        locations = Location.objects.filter(lunch__pk=lunch_pk)

        context = {
            'locations': locations,
            'lunch': lunch
        }
        return context


class VotesView(View):

    def post(self, request, **kwargs):
        lunch_pk = self.kwargs.get('pk')
        lunch = Lunch.objects.get(pk=lunch_pk)
        location_voted_for_id = self.request.POST.get('location')
        selected_location = lunch.location_set.get(pk=location_voted_for_id)
        selected_location.votes += 1
        selected_location.save()
        results_url = reverse('tavern:results', args=(lunch.pk,))
        return HttpResponseRedirect(results_url)
