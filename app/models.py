from django.db import models
from django.urls import reverse


PATIENT_CLASS = [
    ('mom', 'Mom'),
    ('dad', 'Dad'),
    ('single', 'Single'),
    ('caretaker', 'Caretaker'),
]

GENDER = [
    ('female', 'Female'),
    ('male', 'Male'),
]

CAL = [
    ('google', 'Google Calendar'),
    ('apple', 'Apple Calendar'),
    ('outlook', 'Outlook Calendar'),
    ('desk', 'Desk Calendar'),
]

FEELS = [
    ('trust',"I trust my doctor will make the decisions that are of best interest to me."),
    ('opinions', "I have opinions on the matter and would like to learn more about vaccinations."),
    ('oppose', "I am opposed to how often vaccines are administered and would like more information."),
    ('none', "I am not interested in vaccinating my child, myself, or my parent."),
]

class PatientEnroll(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20, choices=GENDER)
    preg = models.BooleanField(name="Are you pregnant or planning to be pregnant?")
    p_class = models.CharField(max_length=20, choices=PATIENT_CLASS, name="Please select from the following:")
    calendar = models.CharField(max_length=20, choices=CAL, name="What calendar do you currently use?")
    schedule = models.BooleanField(name="May we import your schedule?")
    location = models.BooleanField(name="May we track your location?")
    feelings = models.TextField(max_length=200, choices=FEELS, name="How do you feel about vaccines?")
    info = models.BooleanField(name="Would you like more info about vaccines?")
    learning = models.CharField(max_length=500, name="How would you like to learn more about vaccines?")
    advocacy = models.BooleanField(name="Would you be interested in taking part in advocacy?")


class ProviderEnroll(models.Model):
    pass

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
