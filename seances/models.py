from __future__ import unicode_literals

from django.db import models

from movies.models import Movie


class Seance(models.Model):
    film = models.ForeignKey(Movie, on_delete=models.CASCADE)
    starts_at = models.DateTimeField()
    duration = models.IntegerField()
