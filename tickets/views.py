from rest_framework import generics


from models import Ticket
from serializers import TicketSerializer


class TicketListView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        seance_id = self.kwargs['seance_id']
        return Ticket.objects.filter(seance_id=seance_id)
