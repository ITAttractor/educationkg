from django.db import models


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

    def __unicode__(self):
        return '%s (%s - %s)' % (self.full_name, self.school_title, self.location)


