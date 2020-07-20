import datetime
from django.db import models
from django.utils import timezone

class Champion(models.Model):
    name = models.CharField(max_length=200)
    launch_date = models.DateTimeField('date launched')

    def __str__(self):
        return self.name

    def published_recently(self):
        return self.launch_date >= timezone.now() - datetime.timedelta(days=1)



class Data(models.Model):
    champ = models.ForeignKey(Champion, on_delete=models.CASCADE)
    attack_type = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    champ_type = models.CharField(max_length=200)
    role = models.CharField(max_length=200)



