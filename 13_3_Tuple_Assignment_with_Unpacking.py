#June 5 2020
# 13.3. Tuple Assignment with Unpacking

#Example how to iterate through the indexes of a sequence, and thus enumerate the items and their positions in the sequence
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(len(fruits)):
    print(n, fruits[n])
print(">>>Example 1 Completed<<<")
#Same example using enumerate
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for item in enumerate(fruits):
    print(item[0], item[1])
print(">>>Example 2 Completed<<<")
#Example 3 - the pythonic way to solve the same problem
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for index, fruit in enumerate(fruits):
    print(index, fruit)

#Task 1. With only one line of code, assign the variables water, fire, electric, and grass to the values “Squirtle”, “Charmander”, “Pikachu”, and “Bulbasaur”
water, fire, electric, grass = "Squirtle", "Charmander", "Pikachu","Bulbasaur"
print(">>>Task 1 Completed<<<")

#Task 2. With only one line of code, assign four variables, v1, v2, v3, and v4, to the following four values: 1, 2, 3, 4.
v1, v2, v3, v4 = 1,2,3,4
print(">>>Task 2 Completed<<<")

#Task 3. If you remember, the .items() dictionary method produces a sequence of tuples. Keeping this in mind, we have provided you a dictionary called pokemon. For every key value pair, append the key to the list p_names, and append the value to the list p_number. Do not use the .keys() or .values() methods.

pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
p_names = []
p_number = []

for key, value in pokemon.items():
    p_names.append(key)
    p_number.append(value)
print(p_names, p_number)
print(">>>Task 3 Completed<<<")

#Task 4. The .items() method produces a sequence of key-value pair tuples. With this in mind, write code to create a list of keys from the dictionary track_medal_counts and assign the list to the variable name track_events. Do NOT use the .keys() method.

track_medal_counts = {'shot put': 1, 'long jump': 3, '100 meters': 2, '400 meters': 2, '100 meter hurdles': 3, 'triple jump': 3, 'steeplechase': 2, '1500 meters': 1, '5K': 0, '10K': 0, 'marathon': 0, '200 meters': 0, '400 meter hurdles': 0, 'high jump': 1}
track_events = []

for key, value in track_medal_counts.items():
    track_events.append(key)
print(">>>Task 4 Completed<<<")
