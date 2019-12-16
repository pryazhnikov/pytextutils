#!/usr/bin/env python
import re


def parse_time(text_value):
    text_value = str(text_value).strip()

    pattern = r'''
        ^\s*
        (?P<hours>0?\d|1\d|2[0-3])
        \s*:\s*
        (?P<minutes>[0-5]\d)
        (\s*:\s*(?P<seconds>[0-5]\d))?
        \s*
        (?P<day_part>AM|PM|A\.M\.|P\.M\.)
        \s*
        $
        '''
    match = re.search(pattern, text_value, re.IGNORECASE | re.VERBOSE)
    if not match:
        return None

    hours = int(match.group('hours'))
    minutes = int(match.group('minutes'))
    seconds = match.group('seconds')
    if not seconds:
        seconds = 0

    day_part = match.group('day_part').replace('.', '').lower()
    if (day_part == 'pm') and (hours < 12):
        # 11 PM => 23
        hours += 12
    elif (hours == 12) and (day_part == 'am'):
        # 12 AM => 0
        hours -= 12

    return '{:02d}:{:02d}:{:02d}'.format(int(hours), int(minutes), int(seconds))


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
    dates_reg = '^\\s*(?P<day>\\d+)\\s+(?P<month_name>' + month_names_group \
        + ')\\s+((?P<year>20\\d{2})(\\s+года)?)?(\\s*в)?\\s+(?P<hours>\\d|[012]\\d):(?P<minutes>\\d{2})'

    match = re.search(dates_reg, text_value, re.IGNORECASE | re.UNICODE)
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
