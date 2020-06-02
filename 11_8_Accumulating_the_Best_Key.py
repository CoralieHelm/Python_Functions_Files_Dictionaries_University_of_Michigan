#June 1 2020
#11.8. Accumulating the Best Key

#Check your Understanding
#1. Create a dictionary called d that keeps track of all the characters in the string placement and notes how many times each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to min_value.
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

d = {}
for character in placement:
    if character not in d:
        d[character] = 0
    d[character] = d[character] + 1

keys =list(d.keys())
min_value = keys[0]

for key in keys:
    if d[key] < d[min_value]:
        min_value = key
print(min_value)
#You passed: 100.0% of the tests
print("******************")
#5. Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to max_value.
product = "iphone and android phones"
lett_d = {}

for letter in product:
    if letter not in lett_d:
        lett_d[letter] = 0
    lett_d[letter] = lett_d[letter] + 1

letter_keys = list(lett_d.keys())
max_value= letter_keys[0]

for key in letter_keys:
    if lett_d[key] > lett_d[max_value]:
        max_value = key

print(lett_d)
print(letter)
#You passed: 100.0% of the tests
