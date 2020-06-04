#June 4 2020
# 12.10. Functions can call other functions (Composition)

#example Function Composition from previous exercises



def most_common_letter(s):
    frequencies = count_freqs(s)
    return best_key(frequencies)

def count_freqs(st):
    d = {}
    for c in st:
        if c not in d:
             d[c] = 0
        d[c] = d[c] + 1
    return d

def best_key(dictionary):
    ks = dictionary.keys()
    best_key_so_far = list(ks)[0]  # Have to turn ks into a real list before using [] to select an item
    for k in ks:
        if dictionary[k] > dictionary[best_key_so_far]:
            best_key_so_far = k
    return best_key_so_far


print(most_common_letter("hellllllllllooooooo000 woooooooooooorld"))
print("<<<<<<<<<<<<<<<<New Task>>>>>>>>>>>>>>")

#Check your Understanding
#1. Write two functions, one called addit and one called mult. addit takes one
#number as an input and adds 5. mult takes one number as an input, and multiplies that input by whatever is returned by addit, and then returns the result.
def addit(number):
    return number + 5


def mult(numb):
    multi = addit(numb)* numb
    return multi

print("The Result is: ")
print(mult(5))
