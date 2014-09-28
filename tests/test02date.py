# -*- coding: utf-8 -*-
import unittest
import datetime


class DatePattern:

    def __init__(self, year, month, day):
        self.date = datetime.date(year, month, day)
        self.year = year
        self.month = month
        self.day = day

    def matches(self):
        return self.date


class MatchTest(unittest.TestCase):

    def testMatches(self):
        p = DatePattern(2014, 9, 27)
        self.assertEqual(datetime.date.today(), p.matches())

if __name__ == '__main__':
    unittest.main()
