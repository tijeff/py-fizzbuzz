#!/usr/bin/env python
__author__ = "JF Marronnier"
__project__ = "FizzBuzz"


class FizzBuzz:
    def __init__(self):
        pass

    @classmethod
    def say(cls, param):
        return "Buzz" if not param % 10 else str(param)
