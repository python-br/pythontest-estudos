# -*- coding: utf-8 -*-
import unittest


def soma(a, b):
    return a + b


class BasicoTest(unittest.TestCase):

    def test_soma(self):
        resultado = soma(1, 2)
        self.assertEqual(3, resultado)

if __name__ == '__main__':
    unittest.main()
