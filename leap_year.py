import unittest
import pytest

def check_leap (year):
    leap = " is a leap year"
    not_leap = " is not a leap year"

    if (int(year) % 4) == 0:
        if (int(year) % 100) == 0:
            if (int(year) % 400) == 0:
                print(str(year) + leap)
                return 1
            else:
                print(str(year) + not_leap)
                return 0
        else:
            print(str(year) + leap)
            return 1
    else:
        print(str(year) + not_leap)
        return 0


