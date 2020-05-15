from django.db import models


class UserScores(models.Model):

    uid=models.CharField(max_length=32)
    scores=models.IntegerField()

