from pytextutils.datetimes import parse_time, parse_russian_date

import datetime
import unittest


class DateTimesTest(unittest.TestCase):
    TIME_STRING_TEST_CASES = (
        ('1:59  AM', '01:59:00'),
        ('   9:10 pm ', '21:10:00'),
        ('06:30pm', '18:30:00'),
        ('19:00pm', '19:00:00'),  # a human error in the input data
        ('13:10am', '13:10:00'),  # a human error in the input data
        ('12:01 a.m.', '00:01:00'),
        ('12:10p.m.', '12:10:00'),
        ('8 : 20 : 45  A.M.', '08:20:45'),
        ('23:45:30 A.M.', '23:45:30'),  # a human error in the input data
    )

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

    def test_parse_time(self):
        for input_value, expected_time in self.TIME_STRING_TEST_CASES:
            actual_time = parse_time(input_value)
            self.assertEqual(
                expected_time,
                actual_time,
                "Wrong time value found for {}: {}".format(input_value, actual_time)
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
