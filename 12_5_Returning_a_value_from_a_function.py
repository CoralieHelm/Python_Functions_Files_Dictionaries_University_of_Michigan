# June 2 2020
#12.5. Returning a value from a function

#8. Write a function named same that takes a string as input, and simply returns that string.
def same(string):
    return string

#9. Write a function called same_thing that returns the parameter, unchanged.
def same_thing(x):
    return x

#10. Write a function called subtract_three that takes an integer or any number as input, and returns that number minus three.
def subtract_three(n):
    return n - 3

# 11. Write a function called change that takes one number as its input and returns that number, plus 7.
def change(n):
    return n + 7

#12. Write a function named intro that takes a string as input. Given the string “Becky” as input, the function should return: “Hello, my name is Becky and I love SI 106.”
def intro(string):
    return "Hello, my name is " + string + " and I love SI 106."

#13. Write a function called s_change that takes one string as input and returns that string, concatenated with the string ” for fun.”.
def decision(string):
    if len(string) > 17:
        return "This is a long string"
    else:
        return "This is a short string"
