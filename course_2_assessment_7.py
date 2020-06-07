#June 7 2020
#course_2_assessment_7

print("*******Start of Assessment 7*******")

print("<<<<<<<Task 1>>>>>>>")
#Task 1. Create a function called mult that has two parameters, the first is required and should be an integer, the second is an optional parameter that can either be a number or a string but whose default is 6. The function should return the first parameter multiplied by the second.
def mult(integer, str_or_num = 6):
    return integer * str_or_num

print(mult("Hello, Programmer! "))
print("<<<<<<<Task 1 Completed>>>>>>>")

print("<<<<<<<Task 2>>>>>>>")
#Tast 2. The following function, greeting, does not work. Please fix the code so that it runs without error. This only requires one change in the definition of the function.

"""def greeting(greeting="Hello ", name, excl="!"):
    return greeting + name + excl"""
#fixed function:
def greeting(name, greeting="Hello ", excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))
print("<<<<<<<Task 2 Completed>>>>>>>")

print("<<<<<<<Task 3>>>>>>>")
#Task 3. Below is a function, sum, that does not work. Change the function definition so the code works. The function should still have a required parameter, intx, and an optional parameter, intz with a defualt value of 5.
"""def sum(intz=5, intx):
    return intz + intx"""
#function fixed:
def sum(intx, intz=5):
    return intz + intx
print(sum(5))
print("<<<<<<<Task 3 Completed>>>>>>>")

print("<<<<<<<Task 4>>>>>>>")
#Task 4. Write a function, test, that takes in three parameters: a required integer, an optional boolean whose default value is True, and an optional dictionary, called dict1, whose default value is {2:3, 4:5, 6:8}. If the boolean parameter is True, the function should test to see if the integer is a key in the dictionary. The value of that key should then be returned. If the boolean parameter is False, return the boolean value “False”.
def test(number, boolean = True, dict1 = {2:3, 4:5, 6:8}):
    if boolean == True:
        if number in dict1:
            return dict1[number]
    else:
        return False

print(test(2))
print("<<<<<<<Task 4 Completed>>>>>>>")

print("<<<<<<<Task 5>>>>>>>")
#Task 5. Write a function called checkingIfIn that takes three parameters. The first is a required parameter, which should be a string. The second is an optional parameter called direction with a default value of True.
#The third is an optional parameter called d that has a default value of {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}. Write the function checkingIfIn so that when the second parameter is True, it checks to see if the first parameter is a key in the third parameter; if it is, return True, otherwise return False.
#But if the second paramter is False, then the function should check to see if the first parameter is not a key of the third. If it’s not, the function should return True in this case, and if it is, it should return False.
def checkingIfIn(string, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if string in d:
            return True
        else:
            return False
    else:
        if string not in d:
            return True
        else:
            return False

print(checkingIfIn("apple"))
print(checkingIfIn("Python"))
print("<<<<<<<Task 5 Completed>>>>>>>")

print("<<<<<<<Task 6>>>>>>>")
#We have provided the function checkingIfIn such that if the first input parameter is in the third, dictionary, input parameter, then the function returns that value, and otherwise, it returns False. Follow the instructions in the active code window for specific variable assignmemts.


print("<<<<<<<Task 6 Completed>>>>>>>")

print("*******End of Assessment 7*******")
