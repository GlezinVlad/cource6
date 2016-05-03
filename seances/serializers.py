from rest_framework import serializers

from models import Seance


class SeanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seance
        fields = ('id', 'film', 'starts_at', 'duration')
