from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser



class EmploiDuTemps(models.Model):
    emploi_data = models.JSONField(default=dict)
    published_date = models.DateTimeField(blank=True, null=True)
   

    def publish(self):
        self.published_date = timezone.now()


    