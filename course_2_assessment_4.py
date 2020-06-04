#June 4 2020
#course_2_assessment_4
print("*****************Beginning of Assessment 4**************")
#Task 1: Write a function called int_return that takes an integer as input and returns the same integer.
def int_return(integer):
    return integer

print(int_return(5))
print("<<<<<<<<<<<<<<Task 1 Completed>>>>>>>>>>>>>")

#Task 2: Write a function called add that takes any number as its input and returns that sum with 2 added.
def add(number):
    return number + 2

print(add(5))
print("<<<<<<<<<<<<<<Task 2 Completed>>>>>>>>>>>>>")
#Task 3. Write a function called change that takes any string, adds “Nice to meet you!” to the end of the argument given, and returns that new string.
def change(string):

    return string + "Nice to meet you!"
print(change("The Magician "))
print("<<<<<<<<<<<<<<Task 3 Completed>>>>>>>>>>>>>")
#Task 4. Write a function, accum, that takes a list of integers as input and returns the sum of those integers.
def accum(list):
    sum_list = 0
    for item in list:
        sum_list += item
    return sum_list

list_1 = [6,7,8,1,2,3,5]
print(accum(list_1))
print("<<<<<<<<<<<<<<Task 4 Completed>>>>>>>>>>>>>")
#Task 5. Write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to 5, return “Longer than 5”. If the length is less than 5, return “Less than 5”.
def length(list):
    if len(list) >= 5:
        return "Longer than 5"
    else:
        return "Less than 5"

list_1 = [6,7,8,1,2,3,5]
print(length(list_1))
print("<<<<<<<<<<<<<<Task 5 Completed>>>>>>>>>>>>>")
#Task 6. You will need to write two functions for this problem. The first function, divide that takes in any number and returns that same number divided by 2. The second function called sum should take any number, divide it by 2, and add 6. It should return this new number. You should call the divide function within the sum function. Do not worry about decimals.
def divide(number):
    return number / 2

def sum(numb1):
    new_numb = divide(numb1)
    return new_numb + 6

print(sum(5))
print("<<<<<<<<<<<<<<Task 6 Completed>>>>>>>>>>>>>")
print("*****************End of Assessment 4**************")
