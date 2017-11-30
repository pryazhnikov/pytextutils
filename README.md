# Python Text Utils [![Build Status](https://travis-ci.org/pryazhnikov/pytextutils.svg?branch=master)](https://travis-ci.org/pryazhnikov/pytextutils)

This repo contains utility functions for structured data extraction from human readable to machine readable format.

Usage examples:

```python
import pytextutils as tu

import datetime


# Human readable numbers processing
print(tu.numbers.get_int_value(" 1,014\t"))  # 1014
print(tu.numbers.get_int_value("+123,456,789"))  # 123456789
print(tu.numbers.get_int_value("~ 1.3m"))  # 1300000

# Human readable times processing
print(tu.datetimes.parse_time('06:30pm'))  # 18:30:00

# Human readable datetimes processing (in Russian)
today = datetime.date(2017, 11, 30)
print(tu.datetimes.parse_russian_date('04 августа в 6:05', today))  # 2017-08-04 06:05
print(tu.datetimes.parse_russian_date('20 Июня 2015 года 19:30', today))  # 2015-06-20 19:30
```
