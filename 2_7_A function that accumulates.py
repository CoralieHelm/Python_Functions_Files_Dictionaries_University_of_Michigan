# June 2 2020
#2.7. A function that accumulates

#Check your Understanding
#1. Write a function named total that takes a list of integers as input, and returns the total value of all those integers added together.
def total(list_int):
    add = 0
    for int in list_int:
        add = add + int
    return add

#2. 2. Write a function called count that takes a list of numbers as input and returns a count of the number of elements in the list.
def count(list_numbers):
    count = 0
    for number in list_numbers:
        count = count + 1
    return count
