from django.shortcuts import render
from .models import AgeGroup
from rest_framework import generics
from .serializers import VaccineListSerializer
from .models import VaccineList, PatientEnroll
from .forms import PatientForm


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = VaccineList.objects.all()
    serializer_class = VaccineListSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = VaccineList.objects.all()
    serializer_class = VaccineListSerializer


def start(request):
    return render(request, 'start.html')

def cat(request):
    return render(request, 'cat.html')

def patient(request):
    form = PatientForm()
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_prompt.html')
    else:
        PatientForm()
    return render(request, 'patient.html', {'form': form})

def schedule_prompt(request):
    return render(request, 'schedule_prompt.html')

def provider(request):
    return render(request, 'provider.html')

def home(request):
    return render(request, 'home.html')

def age_groups(request):
    groups = AgeGroup.objects.all()
    return render(request, 'age_groups.html', {'groups': groups})
