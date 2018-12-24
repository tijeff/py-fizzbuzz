from unittest import TestCase
from fizzbuzz import FizzBuzz


class TestFizzBuzz(TestCase):
    def test_first(self):
        my_fizzbuzz = FizzBuzz
        self.assertEqual("1", my_fizzbuzz.say(1))

    def test_traite_fizz(self):
        my_fizzbuzz = FizzBuzz
        self.assertEqual("Fizz", my_fizzbuzz.say(3))
