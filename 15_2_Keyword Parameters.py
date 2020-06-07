#June 7 2020
#15.2. Keyword Parameters

#Check your understanding
#advfuncs-2-1: What value will be printed for z?
initial = 7
def f(x, y = 3, z = initial):
    print("x, y, z are:", x, y, z)

f(2, 5)
#D. 7

#advfuncs-2-2: What value will be printed for y?
initial = 7
def f(x, y = 3, z = initial):
    print("x, y, z are:", x, y, z)

f(2, z = 10)
#B. 3

#advfuncs-2-3: What value will be printed for x?
initial = 7
def f(x, y = 3, z = initial):
    print("x, y, z are:", x, y, z)

#f(2, x=5)
#E. Runtime error

#advfuncs-2-4: What value will be printed for z?
initial = 7
def f(x, y = 3, z = initial):
    print ("x, y, z are:", x, y, z)
initial = 0
f(2)
#B. 7

#advfuncs-2-5: What value will be printed below?

names = ["Alexey", "Catalina", "Misuki", "Pablo"]
print("'{first}!' she yelled. 'Come here, {first}! {f_one}, {f_two}, and {f_three} are here!'".format(first = names[1], f_one = names[0], f_two = names[2], f_three = names[3]))
#C. 'Catalina!' she yelled. 'Come here, Catalina! Alexey, Misuki, and Pablo are here!'

#5. Define a function called multiply. It should have one required parameter, a string. It should also have one optional parameter, an integer, named mult_int, with a default value of 10. The function should return the string multiplied by the integer. (i.e.: Given inputs “Hello”, mult_int=3, the function should return “HelloHelloHello”)

def multiply(string, mult_int = 10):
    return string * mult_int
print(multiply("Hello World "))

#6. Currently the function is supposed to take 1 required parameter, and 2 optional parameters, however the code doesn’t work. Fix the code so that it passes the test. This should only require changing one line of code.

def waste(var = "Water", mar, marble = "type"):
    final_string = var + " " + marble + " " + mar
    return final_string
#fixed: the variable "mar" needs to appear before keyword arguments. 

def waste(mar, var = "Water", marble = "type"):
    final_string = var + " " + marble + " " + mar
    return final_string
