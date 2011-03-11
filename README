django-countries
================

django-countries - minimalistic, reusable Django app providing easy-to-use
CountryField for your models

Specification
-------------

countries.models.CountryField is based on CharFields. Its values, stored
in the database are ISO 3166-1 alpha-2, uppercase country codes. It is
represented in HTML forms as a select with uppercase, official English
short country names as its choices.

All country names are marked for lazy translation.

Installation
------------

- copy `countries` directory to your Python path
- add `'countries'` to your settings.INSTALLED_APPS

Usage
-----

An example is worth a thousand words:

    from django.db import models
    from countries.models import CountryField

    class Locality(models.Model)
        name = models.CharField("locality name", max_length=50)
        country = CountryField("country")

That's it.

