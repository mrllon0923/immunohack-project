from django.shortcuts import render
from .models import AgeGroup
from rest_framework import generics
from .serializers import VaccineListSerializer
from .models import VaccineList


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

def patient(request):
    return render(request, 'patient.html')

def provider(request):
    return render(request, 'provider.html')

def age_groups(request):
    groups = AgeGroup.objects.all()
    return render(request, 'age_groups.html', {'groups': groups})
