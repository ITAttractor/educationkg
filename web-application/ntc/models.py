from django.db import models
from django.utils.translation import ugettext_lazy as _


class ParsedNTC(models.Model):
    school_title = models.CharField(max_length=255, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=255, null=False, blank=False)
    math = models.CharField(max_length=5, null=True, blank=True)
    physics = models.CharField(max_length=5, null=True, blank=True)
    chemistry = models.CharField(max_length=5, null=True, blank=True)
    geometry = models.CharField(max_length=5, null=True, blank=True)
    biology = models.CharField(max_length=5, null=True, blank=True)
    geography = models.CharField(max_length=5, null=True, blank=True)
    history = models.CharField(max_length=5, null=True, blank=True)
    eng_lang = models.CharField(max_length=5, null=True, blank=True)
    ger_lang = models.CharField(max_length=5, null=True, blank=True)
    fr_lang = models.CharField(max_length=5, null=True, blank=True)
    kyr_lang = models.CharField(max_length=5, null=True, blank=True)
    rus_lang = models.CharField(max_length=5, null=True, blank=True)
    uzb_lang = models.CharField(max_length=5, null=True, blank=True)
    informatics = models.CharField(max_length=5, null=True, blank=True)
    civics = models.CharField(max_length=5, null=True, blank=True)
    notes = models.CharField(max_length=5, null=True, blank=True)
    integration_queue = models.ForeignKey('IntegrationQueue')

    def __unicode__(self):
        return '%s (%s - %s)' % (self.full_name, self.school_title, self.location)


class IntegrationQueue(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.NullBooleanField()

    def __unicode__(self):
        return "%s - %s" % (self.id, self.timestamp.strftime("%d.%m.%y %H:%M"))


class NTC(models.Model):
    school = models.ForeignKey('schools.School')
    full_name = models.CharField(max_length=255, null=False, blank=False)
    math = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_("Math"))
    physics = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_("Physics"))
    chemistry = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_("Chemistry"))
    geometry = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_("Geometry"))
    biology = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_("Biology"))
    geography = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_("Geography"))
    history = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_("History"))
    eng_lang = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_("English language"))
    ger_lang = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_("German language"))
    fr_lang = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_("French language"))
    kyr_lang = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_("Kyrgyz language"))
    rus_lang = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_("Russian language"))
    uzb_lang = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_("Uzbek language"))
    informatics = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_("Informatics"))
    civics = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_("Civics"))
    notes = models.CharField(max_length=5, null=True, blank=True, verbose_name=_("Notes"))
    parsed_ntc = models.OneToOneField('ParsedNTC')

    def __unicode__(self):
        return '%s - %s - %s' % (self.full_name, self.school.title, self.school.district)
