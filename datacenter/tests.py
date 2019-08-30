from django.test import TestCase
from .models import Visit, Passcard
from datetime import datetime


class VisitModelTest(TestCase):

  @classmethod
  def setUpTestData(cls):
    passcard, created = Passcard.objects.get_or_create(
      owner_name='Bob',
      passcode='bib',
    )

    Visit.objects.create(
      created_at=datetime(year=2018, month=1, day=1, hour=0),
      passcard=passcard,
      entered_at=datetime(year=2019, month=8, day=1, hour=0, minute=0),
      leaved_at=datetime(year=2019, month=8, day=1, hour=1, minute=10),
    )

    Visit.objects.create(
      created_at=datetime(year=2018, month=1, day=1, hour=0),
      passcard=passcard,
      entered_at=datetime(year=2019, month=8, day=1, hour=0, minute=0),
      leaved_at=datetime(year=2019, month=8, day=1, hour=0, minute=20),
    )

  def test_visit_object_is_long(self):

    visit1 = Visit.objects.get(id=1)
    self.assertTrue(visit1.is_long() == True)
    self.assertTrue(visit1.is_long(minutes=120) == False)

    visit2 = Visit.objects.get(id=2)
    self.assertTrue(visit2.is_long(minutes=21) == False)
