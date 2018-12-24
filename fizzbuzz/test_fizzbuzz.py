from unittest import TestCase
from fizzbuzz import FizzBuzz


class TestFizzBuzz(TestCase):
    def test_first(self):
        my_fizzbuzz = FizzBuzz
        self.assertEqual("1", my_fizzbuzz.say(1))
