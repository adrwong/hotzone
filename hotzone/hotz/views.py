from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
import requests
from hotz.models import *
from hotz.forms import *

class VirusList(ListView):
    template_name = "virus_list.html"
    model = Virus

class CreateVirus(CreateView):
    template_name = "createVirus.html"
    model = Virus
    fields = ['name', 'cmName', 'maxInfestPeriod']

class PatientViewVisits(TemplateView):
    template_name = "visit_list.html"

    def get_context_data(self, **kwargs):
        patient = self.kwargs['patient']
        context = super().get_context_data(**kwargs)
        context['visit_list'] = Visit.objects.filter(patient__pk = patient)
        context['patient'] = Patient.objects.get(pk = patient)
        return context

class PatientViewAll(ListView):
    template_name = "patient_list.html"
    model = Patient

class CreatePatient(CreateView):
    template_name = "createPatient.html"
    model = Patient
    fields = ['fName', 'lName', 'dob', 'doc', 'identity', 'virus']

# visit details is incomplete
class visitDetails(TemplateView):
    template_name = "visit_details.html"
    model = Visit

class CreateVisit(CreateView):
    template_name = "createVisit.html"
    model = Visit
    fields = ['startTime', 'endTime', 'tov', 'location', 'patient']
    def get_context_data(self, **kwargs):
        patient = self.kwargs['patient']
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(pk = patient)
        return context

class Locations(TemplateView):
    template_name = "location_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location_list'] = Location.objects.all()
        return context
    
class LocationDetailsFromGeo(CreateView):
    template_name = "createLocationFromGeo.html"
    model = Location
    fields = fields = ['nameEN','addressEN',  'xCoor', 'yCoor']
    def get_context_data(self, **kwargs):
        nameEN = self.kwargs['name']
        addressEN = self.kwargs['address']
        xCoor = self.kwargs['x']
        yCoor = self.kwargs['y']
        context = super().get_context_data(**kwargs)
        context['name'] = nameEN
        context['address'] = addressEN
        context['xCoor'] = xCoor
        context['yCoor'] = yCoor
        return context

    
class createLocation(CreateView):
    template_name = "createLocation.html"
    model = Location
    fields = ['addressEN', 'nameEN', 'xCoor', 'yCoor']

def GeoSearch(request):
    url ='https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q={}'
    form = geoDataForm()
    if request.method == 'POST':
        location = request.POST['nameEN']
        response = requests.get(url.format(location)).json()
    
    else:
        location = ''
        response = ''

    context = {'geoResult_list' : response, 'form' : form}
    return render(request, 'geo_search.html', context)
    


class Home(TemplateView):
    template_name = "home.html"
