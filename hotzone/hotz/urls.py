from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from hotz import views

urlpatterns = [

    path('virusList',
        views.VirusList.as_view(),
        name='virusList'),

    path('createVirus',
        views.CreateVirus.as_view(),
        name='createVirus'),

    path('patientVisits/<int:patient>', 
        views.PatientViewVisits.as_view(),
        name='patient-visits'),

    path('patients',
        views.PatientViewAll.as_view(),
        name='patients'),

    path('createPatient',
        views.CreatePatient.as_view(),
        name='createPatient'),

    path('home', views.Home.as_view(), name ='home'),

    path('createVisit/<int:patient>',
        views.CreateVisit.as_view(),
        name='create-visit'),

    path('locations', views.Locations.as_view(), name='locations'),

    path('createLocation', views.createLocation.as_view(), name='createLocation'),

    path('geoSearch', views.GeoSearch, name='geoSearch'),
    
    path('createLocationFromGeo/<str:name>/<str:address>/<int:x>/<int:y>', 
        views.LocationDetailsFromGeo.as_view(),
        name='createLocationGeo'),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)