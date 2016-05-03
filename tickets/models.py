from __future__ import unicode_literals

from django.db import models

from seances.models import Seance


class Ticket(models.Model):
    seance = models.ForeignKey(Seance, on_delete=models.CASCADE, related_name='tickets')
    row = models.IntegerField()
    place = models.IntegerField()
    user_id = models.IntegerField()

