from django.db import models
from django.urls import reverse


class VaccineList(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class Vaccine(models.Model):
    name = models.CharField(max_length=200)
    dose = models.CharField(max_length=200)
    schedule = models.TextField()
    earliest_dose = models.CharField(max_length=200, blank=True)
    mininum_interval = models.CharField(max_length=200, blank=True)
    contraindications = models.TextField(blank=True)
    protection = models.TextField(blank=True)
    at_risk = models.TextField(blank=True)

    def __str__(self):
        return self.name


class AgeGroup(models.Model):
    group = models.CharField(max_length=200)
    vaccines = models.ManyToManyField(Vaccine)

    def __str__(self):
        return self.group


class Disease(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    transmission = models.TextField()
    incubation_period = models.CharField(max_length=200, blank=True)
    infectious_period = models.CharField(max_length=200, blank=True)
    symptoms = models.TextField()
    vaccine_type = models.CharField(max_length=200, blank=True)
    complications = models.TextField(blank=True)
    severity = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Dose(models.Model):
    pass


class Schedule(models.Model):
    pass


class Symptom(models.Model):
    pass


class Complication(models.Model):
    pass
