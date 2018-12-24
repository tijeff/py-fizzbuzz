from unittest import TestCase
from fizzbuzz import FizzBuzz


class TestFizzBuzz(TestCase):
    def setUp(self):
        self.fizzbuzz = FizzBuzz

    def test_first(self):
        self.assertEqual("1", self.fizzbuzz.say(1))

    def test_traite_fizz(self):
        self.assertEqual("Fizz", self.fizzbuzz.say(3))

    def test_buzz_10(self):
        my_fizzbuzz = FizzBuzz
        self.assertEqual("Buzz", my_fizzbuzz.say(10))
