from django.db import models
import locale
from list import COUNTRIES

class CountryField(models.CharField):
    """
    Model field based on CharField, containing ISO 3166-1 alpha-2 country codes and representing
    them as uppercase, official English short country names. Defaults `max_length` to 2 and
    `choices` to country list.
    """

    def __init__(self, *args, **kwargs):
        choices = ((code, unicode(name)) for code, name in COUNTRIES)
        locale.setlocale(locale.LC_ALL, '')
        choices = sorted(choices, lambda x, y: locale.strcoll(x[1], y[1]))
        local_kwargs = {
            'max_length': 2,
            'choices': choices,
        }
        local_kwargs.update(kwargs)
        super(CountryField, self).__init__(*args, **local_kwargs)

from south_introspection_rules import *

