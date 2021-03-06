#!/usr/bin/env python
__author__ = "JF Marronnier"
__project__ = "FizzBuzz"


class FizzBuzz:
    def __init__(self):
        pass

    @classmethod
    def say(cls, param):
        return "FizzBuzz" if not param % 15 else "Fizz" if not param % 3 else "Buzz" if not param % 10 else str(param)
