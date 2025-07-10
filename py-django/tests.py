#### Django’s unit tests use a Python standard library module: unittest. This module defines tests using a class-based approach.
#### Once you’ve written tests, run them using the test command of your project’s manage.py utility:
#### `./manage.py test`

# Run all the tests in the animals.tests module
# $ ./manage.py test animals.tests

# Run all the tests found within the 'animals' package
# $ ./manage.py test animals

# Run just one test case class
# $ ./manage.py test animals.tests.AnimalTestCase

# Run just one test method
# $ ./manage.py test animals.tests.AnimalTestCase.test_animals_can_speak

# Run just a path
# $ ./manage.py test animals/

# Run using pattern
# $ ./manage.py test --pattern="tests_*.py"

from django.test import TestCase
from myapp.models import Animal


class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
