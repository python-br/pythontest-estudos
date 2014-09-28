# -*- coding: utf-8 -*-
import random
import unittest


def gen_age():
    # gera numeros inteiros entre 15 e 99
    return random.randint(15, 99)


class AgeTest(unittest.TestCase):

    def setUp(self):
        self.a = gen_age()

    def test_choice(self):
        element = random.choice(self.a)
        self.assertTrue(element in self.a)

    def test_sample(self):
        # with self.assertRaises(ValueError):
        #     random.sample(self.a, 20)
        for element in random.sample(self.a, 5):
            self.assertTrue(element in self.a)

if __name__ == '__main__':
    unittest.main()
