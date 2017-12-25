# Now, we want to ask ourselves the question: How many occurrences of
# the number 9 appear in our randomly made list?
#
# For example, if we have a list: [2,8,9,9,4,5,9], we want to figure out
# how to loop through the list and count the number of occurrences of the
# number 9. In the example list above, the number 9 occurs three times.

import random

# 1. Create random list of integers using while loop
random_list = []
list_length = 20

while len(random_list) < list_length:
  random_list.append(random.randint(0,10))

# Write code here to loop through the list and count all occurrences
# of the number 9. Note that `if` statements and `while` loops will help you solve
# this problem.
def countAllOccurrences(random_list):
    count = 0
    occurrences=0

    while count < list_length:
        # if str(random_list[count]) == '9':
        if random_list[count] == 9:
            occurrences = occurrences +1
        count = count +1

    return occurrences

# Test: If the `while` loop we wrote works, we should manually count
# how many times the number 9 is present in the list.
print random_list
occurrences = countAllOccurrences(random_list)
print occurrences
