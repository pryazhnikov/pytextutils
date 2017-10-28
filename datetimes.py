#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import re
import unittest


def parse_russian_date(text_value, now_dt):
    month_name_to_numbers = {
        'января': 1,
        'февраля': 2,
        'марта': 3,
        'апреля': 4,
        'мая': 5,
        'июня': 6,
        'июля': 7,
        'августа': 8,
        'сентября': 9,
        'октября': 10,
        'ноября': 11,
        'декабря': 12,
    }

    text_value = str(text_value)

    month_names_group = '|'.join(month_name_to_numbers.keys())
    dates_reg = '^\s*(?P<day>\d+)\s+(?P<month_name>' + month_names_group \
        + ')\s+((?P<year>20\d{2})(\s+года)?)?(\s*в)?\s+(?P<hours>\d|[012]\d):(?P<minutes>\d{2})'

    match = re.search(dates_reg, text_value, re.IGNORECASE)
    if not match:
        return None

    date = match.group('day')

    month_name = match.group('month_name').lower()
    month = month_name_to_numbers[month_name]

    year = match.group('year')
    if not year:
        current_year = now_dt.year
        year = current_year

    hours = match.group('hours')
    minutes = match.group('minutes')

    return "{:04d}-{:02d}-{:02d} {:02d}:{:s}".format(int(year), int(month), int(date), int(hours), minutes)


class DateTimesTest(unittest.TestCase):
    RUSSIAN_DATE_TEST_CASES = (
        ('2017-10-28', '1 января в 12:13', '2017-01-01 12:13'),
        ('2017-10-28', '12 февраля    12:13', '2017-02-12 12:13'),
        ('2017-10-28', '23 марта    в    15:45', '2017-03-23 15:45'),
        ('2017-10-28', '30  апреля 2012 года 23:57', '2012-04-30 23:57'),
        ('2017-10-28', '29 мая 2015 года 08:05', '2015-05-29 08:05'),
        ('2017-10-28', '20 Июня 2015 года 19:30', '2015-06-20 19:30'),
        ('2017-10-28', '31 ИЮЛЯ 2016 ГОДА 21:55', '2016-07-31 21:55'),
        ('2017-10-28', '04 августа в 6:05', '2017-08-04 06:05'),
        ('2016-10-28', '8 сентября в 16:40', '2016-09-08 16:40'),
    )

    def test_parse_russian_date(self):
        for now_str, input_value, expected_date_time in self.RUSSIAN_DATE_TEST_CASES:
            now = datetime.datetime.strptime(now_str, "%Y-%m-%d")
            actual_date_time = parse_russian_date(input_value, now)
            self.assertEqual(
                expected_date_time,
                actual_date_time,
                "Wrong datetime value found for {}: {}".format(input_value, actual_date_time)
            )


if __name__ == '__main__':
    unittest.main()
