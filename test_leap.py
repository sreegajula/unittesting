import unittest
import pytest
import leap_year

class test_leap(unittest.TestCase):
    def test_lpyear(self):
        self.assertEqual(leap_year.check_leap(2000), 0)

class test_leap_1(unittest.TestCase):
    def test_lpyear(self):
        self.assertEqual(leap_year.check_leap(0), 1)


def test_answer():
    assert leap_year.check_leap(2000) == 0

def test_answer_1():
    assert leap_year.check_leap(2000) == 1
