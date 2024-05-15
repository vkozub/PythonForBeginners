"""Module providing Regex."""

import re

chars = input('Sequence of cgars separated by comma: ')
# Get list of chars
chars_as_string_list = re.split(r',\s*', chars)
# Slice 2 lists of char
chars_sequence_1 = chars_as_string_list[:int(len(chars_as_string_list)/2)]
chars_sequence_2 = chars_as_string_list[int(len(chars_as_string_list)/2):]

print(chars_sequence_1, chars_sequence_2)
