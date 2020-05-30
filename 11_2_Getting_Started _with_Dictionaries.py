#May 30th 2020
#11.2. Getting Started with Dictionaries

#dictionaries-1-1: A dictionary is an unordered collection of key-value pairs.
#B. True ✔️ Yes, dictionaries are associative collections meaning that they store key-value pairs.

#dictionaries-1-2: What is printed by the following statements?

mydict = {"cat":12, "dog":6, "elephant":23}
print(mydict["dog"])
# B.6

#3. Create a dictionary that keeps track of the USA’s Olympic medal count.
#Each key of the dictionary should be the type of medal (gold, silver, or bronze) and each key’s value should be the number of that type of medal the USA’s won. Currently, the USA has 33 gold medals, 17 silver, and 12 bronze. Create a dictionary saved in the variable medals that reflects this information.
medals = {"gold" : 33, "silver" : 17, "bronze" : 12}
print(medals)
#You passed: 100.0% of the tests

#4. You are keeping track of olympic medals for Italy in the 2016 Rio Summer Olympics! At the moment, Italy has 7 gold medals, 8 silver metals, and 6 bronze medals. Create a dictionary called olympics where the keys are the types of medals,
#and the values are the number of that type of medals that Italy has won so far.
olympics = {"gold" : 7}
olympics["silver"] = 8
olympics["bronze"] = 6
print(olympics)
#You passed: 100.0% of the tests
