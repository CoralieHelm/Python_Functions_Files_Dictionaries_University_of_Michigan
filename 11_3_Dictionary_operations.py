#May 30th 2020
#11.3. Dictionary operations

#dictionaries-2-1: What is printed by the following statements?
mydict = {"cat":12, "dog":6, "elephant":23}
mydict["mouse"] = mydict["cat"] + mydict["dog"]
print(mydict["mouse"])
#c. 18 ✔️ Yes, add the value for cat and the value for dog (12 + 6) and create a new entry for mouse

#2. Update the value for “Phelps” in the dictionary swimmers to include his medals from the Rio Olympics by adding 5 to the current value (Phelps will now have 28 total medals).
#Do not rewrite the dictionary.

swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}
swimmers['Phelps'] = swimmers["Phelps"] + 5
#You passed: 100.0% of the tests
