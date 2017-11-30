from pytextutils.numbers import get_int_value

import unittest


class NumbersTest(unittest.TestCase):
    NUMBER_TEST_CASES = (
        ('25', 25),
        ('-25', -25),
        (' –875', -875),  # &minus; instead of "-"
        ('1,234', 1234),
        ('-1,234', -1234),
        ('+123,456,789', 123456789),
        (" 1,014\t", 1014),
        ('1,234,567', 1234567),
        ('1.5k', 1500),
        ('2.5m', 2500000),
        ('~46k  ', 46000),
        ('~1.3m', 1300000),
        ('2 974 414 970', 2974414970),
        ('4M', 4000000),
        ('3,2B', 3200000000),
    )

    def test_get_int_value(self):
        for input_value, expected_number in self.NUMBER_TEST_CASES:
            actual_number = get_int_value(input_value)
            self.assertEqual(
                expected_number,
                actual_number,
                "Wrong number value found for {}".format(input_value)
            )
