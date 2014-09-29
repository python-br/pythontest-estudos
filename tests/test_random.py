# -*- coding: utf-8 -*-
import random
import unittest


def gen_age():
    # gera numeros inteiros entre 15 e 99
    return random.randint(15, 99)


class AgeTest(unittest.TestCase):

    def setUp(self):
        self.a = gen_age()

    def test_gen_age(self):
        self.assertTrue(self.a >= 15 and self.a <= 99)


if __name__ == '__main__':
    unittest.main()
