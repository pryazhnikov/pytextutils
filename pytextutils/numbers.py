#!/usr/bin/env python
import re


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
