#June 1 2020
#11.7. Accumulating Results From a Dictionary

#Recreation of scrabble execise
scarlet_file = open ("a_study_in_scarlet.txt", "r")
txt = scarlet_file.read() # txt is one long string with all characters

dict = {} #creation of an empty Dictionary

for character in txt:
    if character not in dict:
        #checking if the character is not already in the Dictionary. If it is
        #not, we  initialize the counter
        dict[character] = 0
    dict[character] = dict[character] + 1
    #if the character is already in the Dictionary, we increment its counter
letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f':4, 'g': 2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}
# a list of scrabble letters values

total = 0 # we are setting the total counter to 0

for letter in dict:
    if letter in letter_values:
        total = total + letter_values[letter] * dict[letter]
print(total)
print("**********")

#Check your Understanding
#The dictionary travel contains the number of countries within each continent
#that Jackie has traveled to. Find the total number of countries that Jackie has been to, and save this number to the variable name total.
travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}

total = 0

for countries in travel:
    total = total + travel[countries]

print(total)
#You passed: 100.0% of the tests
print("******************")
#2. schedule is a dictionary where a class name is a key and its value is how many credits it was worth. Go through and accumulate the total number of credits that have been earned so far and assign that to the variable total_credits.
schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3, "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4, "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4}
total_credits = 0

for course in schedule:
    total_credits = total_credits + schedule[course]
print(total_credits)
#You passed: 100.0% of the tests
