from django.db import models
from django.utils.translation import ugettext_lazy as _


class Region(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, unique=True, verbose_name=_("Title"))
    slug = models.CharField(max_length=20, null=True, blank=True, unique=True)
    prepositional_case = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.title


class District(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, unique=True, verbose_name=_("Title"))
    region = models.ForeignKey(Region)

    def __unicode__(self):
        return self.title
