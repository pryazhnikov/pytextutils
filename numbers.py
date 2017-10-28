#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import unittest


def get_int_value(text_value):
    """
    Parses text based numbers: 25 / 1,234 / 1,234,567 / 1.5k, / 2.5m
    """

    # " 123 " -> "123"
    text_value = str(text_value).strip()

    # &minus; sign -> "-"
    text_value = text_value.replace('–', '-')

    # "123 456" -> "123456"
    text_value = text_value.replace(' ', '')

    # "~1000" -> "1000"
    text_value = re.sub(r'^~', '', text_value)

    # "1,234,567" -> "1234567"
    # 12,3k / 1,2m should be ignored
    if re.match(r'^[+-]?\d+(,\d+)+$', text_value):
        text_value = text_value.replace(',', '')

    # Values to parse: 12.3k / 1.2m
    match = re.match(r'^(\d+(?:[,\.]\d+)*)([kmb])$', text_value, re.IGNORECASE)
    if match:
        suffix = match.group(2).lower()
        number = float(match.group(1).replace(',', '.'))
        if suffix == 'k':
            number = 1e3 * number
        elif suffix == 'm':
            number = 1e6 * number
        elif suffix == 'b':
            number = 1e9 * number

        return int(number)

    # Values to parse: 1,234
    if re.match(r'^\d+[,\.]\d+$', text_value):
        text_value = text_value.replace(',', '').replace('.', '')
        return int(text_value)

    # Values to parse: 123
    return int(text_value)


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


if __name__ == '__main__':
    unittest.main()
