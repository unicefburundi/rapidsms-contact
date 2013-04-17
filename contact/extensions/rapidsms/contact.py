from django.db import models

from rapidsms.models import ContactBase

class DemographicContact(models.Model):
    """
    This extension for Contacts allows developers to tie a Contact to
    the Location object they're reporting from.
    """
    birthdate = models.DateTimeField(null=True)
    gender = models.CharField(
            max_length=1,
            choices=(('M', 'Male'), ('F', 'Female')), null=True)
    colline = models.ForeignKey('locations.Location', blank=True, null=True, related_name='colline_dwellers')
    colline_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True
