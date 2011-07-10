from django.utils import unittest
from django.db import models
from django.utils.functional import Promise
import datetime
import re
from list import *
from fields import *

class ThreadTestCase(unittest.TestCase):
    
    def setUp(self):
        pass

    def testLastUpdateIsPast(self):
        self.assertLessEqual(COUNTRIES_LAST_UPDATE, datetime.datetime.now())

    def testCountryListCodes(self):
        code_re = re.compile(r'^[A-Z]{2}$')
        for code, name in COUNTRIES:
            self.assertRegexpMatches(code, code_re)

    def testCountryListNames(self):
        for code, name in COUNTRIES:
            # is name translantable?
            self.assertTrue(isinstance(name, Promise))

    def testCountryField(self):
        field = CountryField()
        # is it CharField-based?
        self.assertTrue(isinstance(field, models.CharField))
        self.assertEqual(field.max_length, 2)

