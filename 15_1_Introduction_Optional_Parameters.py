#June 7 2020
#15.1. Introduction: Optional Parameters
#Check your understanding
#advfuncs-1-1: What will the following code print?

def f(x = 0, y = 1):
    return x * y

print(f())
#A. 0

advfuncs-1-2: What will the following code print?
def f(x = 0, y = 1):
    return x * y

print(f(1))
#B. 1

#Task 1. Write a function called str_mult that takes in a required string parameter and an optional integer parameter. The default value for the integer parameter should be 3. The function should return the string multiplied by the integer parameter.

def str_mult(string, integer = 3):
    return string * integer
