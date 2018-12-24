from unittest import TestCase
from fizzbuzz import FizzBuzz


class TestFizzBuzz(TestCase):
    def setUp(self):
        self.fizzbuzz = FizzBuzz

    def test_first(self):
        self.assertEqual("1", self.fizzbuzz.say(1))

    def test_fizz_3(self):
        self.assertEqual("Fizz", self.fizzbuzz.say(3))

    def test_buzz_10(self):
        self.assertEqual("Buzz", self.fizzbuzz.say(10))

    def test_fizzbuzz_30(self):
        self.assertEqual("FizzBuzz", self.fizzbuzz.say(30))
