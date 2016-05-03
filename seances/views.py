from rest_framework import generics

from models import Seance
from serializers import SeanceSerializer


class SeanceListView(generics.ListCreateAPIView):
    queryset = Seance.objects.all()
    serializer_class = SeanceSerializer


class SeanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seance.objects.all()
    serializer_class = SeanceSerializer
