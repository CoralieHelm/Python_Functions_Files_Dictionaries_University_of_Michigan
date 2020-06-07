# June 7 2020
#course_2_assessment_6
print("******Start of Assessment 6 from Course 2******")

print("<<<<<<Task 1>>>>>>")
# Task 1. Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).
def sublist(list):
    sublist = []
    list_index_counter = 0

    while list_index_counter < len(list) and list[list_index_counter] != 5:
        sublist.append(list[list_index_counter])
        list_index_counter = list_index_counter + 1
    return sublist

list1 = [2,6,13, 2, "hello", 5, 6, 8]
print(sublist(list1))

print("<<<<<<Task 2>>>>>>")
#Task 2. Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.
def check_nums(list):
    new_list1 = []
    number_counter = 0

    while number_counter < len(list) and list[number_counter] != 7:
        new_list1.append(list[number_counter])
        number_counter += 1
    return new_list1

list1 = [2,6,13,7, 2, "hello", 5, 6, 8]
print(check_nums(list1))


print("<<<<<<Task 3>>>>>>")
#Task 3. Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).

def sublist(list_str):
    new_sub_list = []
    string_count = 0

    while string_count < len(list_str) and list_str[string_count] != "STOP":
        new_sub_list.append(list_str[string_count])
        string_count += 1
    return new_sub_list

string_lst = ["Hello", "Good Day", "The world is beautiful", "STOP", "Python"]
print(sublist(string_lst))


print("<<<<<<Task 4>>>>>>")
#Task 4. Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a new list until the string that appears is “z”. The function should return the new list.


def stop_at_z(lst_string):
    new_string_lst = []
    str_counter = 0

    while str_counter < len(lst_string) and lst_string[str_counter] != "z":
        new_string_lst.append(lst_string[str_counter])
        str_counter += 1
    return new_string_lst

string_lst = ["Hello", "Good Day", "zoo", "The world is beautiful", "STOP", "Python", "z"]
print(stop_at_z(string_lst))


print("<<<<<<Task 5>>>>>>")
#Task 5. Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, but using a while loop instead of a for loop. Assign the accumulated total in the while loop code to the variable sum2. Once complete, sum2 should equal sum1.

sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x

sum2 = 0
counter = 0

while counter < len(lst):
    sum2 += lst[counter]
    counter += 1

print("The sum of 'sum1' is: ", sum1)
print("The sum of 'sum2' is: ", sum2)


print("<<<<<<Task 6>>>>>>")
#Task 6. Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing

def beginning(list):
    first_ten = []
    element_counter = 0

    while element_counter < len(list) and list[element_counter] != "bye" :
        if element_counter < 10:
            first_ten.append(list[element_counter])
            element_counter += 1
        else:
            element_counter += 1
    return first_ten

str1 = ["hello", "world", "I", "love", "Pyhton", "bye", "this is great"]

print(beginning(str1))
print("******End of Assessment 6******")
