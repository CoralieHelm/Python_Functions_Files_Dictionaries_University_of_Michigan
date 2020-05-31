swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}

for key in swimmers.keys():
  print(key, "has the value: ", swimmers[key])

keys = list(swimmers.keys())
print(keys)

#Check your understanding

#dictionaries-3-1: What is printed by the following statements?

mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
answer = mydict.get("cat")//mydict.get("dog")
print(answer)
# A. 2 ✔️ get returns the value associated with a given key so this divides 12 by 6.

#dictionaries-3-2: What is printed by the following statements?
mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
print("dog" in mydict)
#A. True ✔️ Yes, dog is a key in the dictionary.

#dictionaries-3-3: What is printed by the following statements?

mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
print(23 in mydict)
#B. False ✔️ Yes, the in operator returns True if a key is in the dictionary, False otherwise.

#dictionaries-3-4: What is printed by the following statements?
total = 0
mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
for akey in mydict:
   if len(akey) > 3:
      total = total + mydict[akey]
print(total)
#B. 43 ✔️ Yes, the for statement iterates over the keys. It adds the values of the keys that have length greater than 3.

#5. Every four years, the summer Olympics are held in a different country. Add a key-value pair to the dictionary places that reflects that the 2016 Olympics were held in Brazil. Do not rewrite the entire dictionary to do this!

places = {"Australia":2000, "Greece":2004, "China":2008, "England":2012}
places["Brazil"] = 2016
#You passed: 100.0% of the tests

#6. We have a dictionary of the specific events that Italy has won medals in and the number of medals they have won for each event. Assign to the variable events a list of the keys from the dictionary medal_events.

medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}
events = list(medal_events.keys())
print(events)
#You passed: 100.0% of the tests
