from django.db import models


class School(models.Model):
    title = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    district = models.ForeignKey('geo.District')
