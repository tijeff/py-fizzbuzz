#!/usr/bin/env python
__author__ = "JF Marronnier"
__project__ = "FizzBuzz"


class FizzBuzz:
    @classmethod
    def say(cls, param):
        return "Fizz" if param == 3 else str(param)
