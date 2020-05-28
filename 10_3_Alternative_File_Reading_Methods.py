#May 28 2020
#May 28 2020
#Python Functions, Files, and Dictionaries - University of Michigan
#Week 1
#10.3. Alternative File Reading Methods
#Check your Understanding

#1. Using the file school_prompt2.txt, find the number of characters in the file and assign that value to the variable num_char.
fileref = open("school_prompt2.txt", "r")
content = fileref.read()
num_char = len(content)
print(num_char)
#You passed: 100.0% of the tests

#2. Find the number of lines in the file, travel_plans2.txt, and assign it to the variable num_lines.
file_ref1 = open("travel_plans2.txt", "r")
content_1 = file_ref1.readlines()
num_lines = len(content_1)
print(num_lines)
#3. Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.

file_ref2 = open("emotion_words2.txt", "r")
content2 = file_ref2.read()
first_forty = content2[:40]
print(first_forty)
#You passed: 100.0% of the tests
