
"""Module providing Regex."""

import re

nums = input('Sequence of numbers: ')
# Get list of numbers
nums_as_string_list = re.split(r'\D+', nums)
nums_list = [int(x) for x in nums_as_string_list]
# Sort it
nums_list.sort()

print(nums_list)
print(type(nums_list))
