#May 31 2020
#11.6. Introduction: Accumulating Multiple Results In a Dictionary

#Notes: “A Study in Scarlet”, by Sir Arthur Conan Doyle can be found on gutenberg.org https://www.gutenberg.org/files/244/244-h/244-h.htm
#The text was downloaded and saved in a txt. file


with open("a_study_in_scarlet.txt", "r") as scarlet:
    scarlet_txt = scarlet.read()
    dict = {} # start with an empty dictionary

    for char in scarlet_txt:
        if char not in dict:
            #if the character is not yet in the dictionary we initialize a counter with 0
            dict[char] = 0
            # if the chatacter is already in the dictionary we increment its counter by 1
        dict[char] = dict[char] + 1
    print("The letter 'c' is occurring " + str(dict["c"]) , "times.")
    print("The letter 'h' is occurring " + str(dict["h"]) , "times.")
    print("The letter 'j' is occurring " + str(dict["j"]) , "times.")
    print("The letter 'a' is occurring " + str(dict["a"]) , "times.")

#Check your understanding
#dictionaries-5-1: Which of the following will print out True if there are more occurrences of e than t in the text of A Study in Scarlet, and False if t occurred more frequently
#(assumming that the previous code, from dict_accum_5, has already run.)
#B. print(x['e'] > x['t']) ✔️ x is the dictionary of counts; you want to compare the values associated with 'e' and 't'.

#Task 2:
with open("a_study_in_scarlet.txt", "r") as scarlet:
    scarlet_txt = scarlet.read()
    dict = {} # start with an empty dictionary

    for char in scarlet_txt:
        if char not in dict:
            #if the character is not yet in the dictionary we initialize a counter with 0
            dict[char] = 0
            # if the chatacter is already in the dictionary we increment its counter by 1
        dict[char] = dict[char] + 1

    for char in dict.keys():
        print(char + ": " + str(dict[char]) + " occurrences.")
        print("***************************")

# Task 3
#2. Provided is a string saved to the variable name sentence. Split the string into a list of words, then create a dictionary that contains each word and the number of times it occurs.
#Save this dictionary to the variable name word_counts.
sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
sentence_lst = sentence.split(" ")

word_counts = {}
for word in sentence_lst:
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] = word_counts[word] + 1

print(word_counts)
#You passed: 100.0% of the tests
print("**********************")

#3. Create a dictionary called char_d from the string stri, so that the key is a character and the value is how many times it occurs.
stri = "what can I do"
char_d = {}
for char in stri:
    if char not in char_d:
        char_d[char] = 0
    char_d[char] = char_d[char] + 1
print(char_d)
#You passed: 100.0% of the tests
