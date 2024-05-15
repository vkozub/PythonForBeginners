"""Module providing Regex."""

import re

chars = input('Sequence of cgars separated by comma: ')
# Get list of chars
chars_as_string_list = re.split(r',\s*', chars)
third_chars_list = chars_as_string_list[2::3]

print(third_chars_list)
