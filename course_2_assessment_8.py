#June 9 2020
#course_2_assessment_8

print("********Start of Assessment 8********")
print("<<<<<<<<Task 1>>>>>>>>")
#Task 1. Sort the following string alphabetically, from z to a, and assign it to the variable sorted_letters.
letters = "alwnfiwaksuezlaeiajsdl"

sorted_letters = sorted(letters, reverse = True)
print(sorted_letters)
print("<<<<<<<<End of Task 1>>>>>>>>")
print()

print("<<<<<<<<Task 2>>>>>>>>")
#Task 2. Sort the list below, animals, into alphabetical order, a-z. Save the new list as animals_sorted.
animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']

animals_sorted = sorted(animals)
print(animals_sorted)
print("<<<<<<<<End of Task 2>>>>>>>>")
print()

print("<<<<<<<<Task 3>>>>>>>>")
#Task 3. The dictionary, medals, shows the medal count for six countries during the Rio Olympics. Sort the country names so they appear alphabetically. Save this list to the variable alphabetical.
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
alphabetical = sorted(medals)
print(alphabetical)
print("<<<<<<<<End of Task 3>>>>>>>>")
print()

print("<<<<<<<<Task 4>>>>>>>>")
#Task 4. Given the same dictionary, medals, now sort by the medal count. Save the three countries with the highest medal count to the list, top_three.
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

def return_keys(key,dictionary):
    return dictionary[key]

ks = medals.keys()

top_three = sorted(ks,key=lambda k : return_keys(k,medals),reverse = True)[:3]
print(top_three)
print("<<<<<<<<End of Task 4>>>>>>>>")
print()

print("<<<<<<<<Task 5>>>>>>>>")
# Task 5. We have provided the dictionary groceries. You should return a list of its keys, but they should be sorted by their values, from highest to lowest. Save the new list as most_needed.

groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}

def return_keys(key, dictionary):
    return dictionary[key]

ks = groceries.keys()

most_needed = sorted(ks, key = lambda k :return_keys(k, groceries), reverse = True)
print(most_needed)
print("<<<<<<<<End Task 5>>>>>>>>")
print()

print("<<<<<<<<Task 6>>>>>>>>")
#Task 6. Create a function called last_four that takes in an ID number and returns the last four digits. For example, the number 17573005 should return 3005. Then, use this function to sort the list of ids stored in the variable, ids, from lowest to highest. Save this sorted list in the variable, sorted_ids. Hint: Remember that only strings can be indexed, so conversions may be needed.
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

def last_four(id_number):

    return (str(id_number)[5:9])

print(last_four(ids))

sorted_ids = sorted(ids, key=last_four )
print(sorted_ids)
print("<<<<<<<<End of Task 6>>>>>>>>")
print()

print("<<<<<<<<Task 7>>>>>>>>")
#Task 7. Sort the list ids by the last four digits of each id. Do this using lambda and not using a defined function. Save this sorted list in the variable sorted_id.
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_id = sorted(ids, key = lambda last: str(last)[4:9])
print(sorted_id)
print("<<<<<<<<End of Task 7>>>>>>>>")
print()

print("<<<<<<<<Task 8>>>>>>>>")
#Sort the following list by each element’s second letter a to z. Do so by using lambda. Assign the resulting value to the variable lambda_sort.
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

lambda_sort = sorted(ex_lst, key = lambda second_letter: second_letter[1])
print(lambda_sort)
print("<<<<<<<<End of Task 8>>>>>>>>")
print()
print("********End of Assessment 8********")
