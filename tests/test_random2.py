import random
import unittest
try:
    from unittest.mock import patch
except ImportError:
    # < python 3.3
    from mock import patch


class Die():

    def roll(self):
        return random.randint(15, 99)


@patch('random.randint', return_value=3)
class TestDice(unittest.TestCase):

    def test_standard_size(self, mocked_randint):
        die = Die()
        result = die.roll()

        mocked_randint.assert_called_with(15, 99)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
