from django.shortcuts import render
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

        context = {

        }
        return context


class VotesView(View):

    def post(self, request, **kwargs):
        # vote_pk = self.kwargs.get('pk')
        # vote = Vote.objects.get(pk=vote_pk)
        print('')