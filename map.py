#June 23 2020
#23.2. Map¶

#Check Your Understanding
#1. Using map, create a list assigned to the variable greeting_doubled that doubles each element in the list lst.

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

def double(lst):
  return lst *2



greeting_doubled = map(double, lst)
print(list(greeting_doubled))

#2. Below, we have provided a list of strings called abbrevs. Use map to produce a new list called abbrevs_upper that contains all the same strings in upper case.

abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

def upper_case(string):
    return string.upper()

abbrevs_upper = map(upper_case, abbrevs)
print(list(abbrevs_upper))
