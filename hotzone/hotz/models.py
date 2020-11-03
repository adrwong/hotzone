from django.db import models
from django.urls import reverse

class Virus(models.Model):
    name = models.CharField(max_length=200)
    # cmName = Common Name
    cmName = models.CharField(max_length=200)
    maxInfestPeriod = models.IntegerField(default=0)
    def __str__(self):
        return self.cmName
    def get_absolute_url(self):
        return reverse('virusList', kwargs={})

class Location(models.Model):
    addressEN = models.CharField(max_length=200)
    nameEN = models.CharField(max_length=200)
    xCoor = models.DecimalField(max_digits=14, decimal_places=8)
    yCoor = models.DecimalField(max_digits=14, decimal_places=8)
    def get_absolute_url(self):
        return reverse('locations', kwargs={})
    def __str__(self):
        return self.nameEN

class Patient(models.Model):
    fName = models.CharField(max_length=200)
    lName = models.CharField(max_length=200)
    # Date of Birth
    dob = models.DateField()
    # Date of Confirmation
    doc = models.DateField()
    identity = models.CharField(max_length=20)
    virus = models.ForeignKey(Virus, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.fName}_{self.identity}'
    def get_absolute_url(self):
        return reverse('patients', kwargs={})

class Visit(models.Model):
    pkn = models.AutoField(primary_key=True)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    # tov = Type Of Visit
    tov = models.CharField(max_length=10)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('patient-visits', args={self.patient.pk})
    def __str__(self):
        return f'({self.patient})({self.tov}){self.location}'

