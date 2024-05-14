
"""Module providing Regex."""

import re

nums = input('Sequence of numbers: ')
# Get list of numbers
nums_as_string_list = re.split(r'\D+', nums)
nums_list = [int(x) for x in nums_as_string_list]
# Get Set with unique numbers
unique_nums = set(nums_list)
# Create a list of unique numbers
sorted_list_of_nums = list(unique_nums)
# Sort it
sorted_list_of_nums.sort()

# Print output as a String
print(', '.join([str(x) for x in sorted_list_of_nums]))

# Find numbers of duplications
for number in sorted_list_of_nums:
    print(f'Amount of duplications of {number}: ', nums_list.count(number))
