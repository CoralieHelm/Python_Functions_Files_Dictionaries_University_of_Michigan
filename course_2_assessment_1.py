#May 29 2020
#Python Functions, Files, and Dictionaries - University of Michigan
#Week 1
#course_2_assessment_1

#Task 1. The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.

travel_file = open("travel_plans.txt" ,"r")
travel = travel_file.read()
num = len(travel)

print(num)
travel_file.close()

#You passed: 100.0% of the tests

print("************")
#Task 2. We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.
num_words = 0
file_ref = "emotion_words.txt"

with open(file_ref, 'r') as file:
    for word in file:
        num_words += len(word.split())
print(num_words)
#You passed: 100.0% of the tests

print("************")
#Task 3. Assign to the variable num_lines the number of lines in the file school_prompt.txt.
file_ref2 = "school_prompt.txt"

with open(file_ref2, "r") as f2:
    f2_lines = f2.readlines()
    num_lines = len(f2_lines)
print(num_lines)
#You passed: 100.0% of the tests

print("************")
#Task 4. Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
with open ("school_prompt.txt", "r") as sp_file:
    beginning_chars = ''
    for character in sp_file.read()[:30]:
        beginning_chars += character
print(beginning_chars)       
#You passed: 100.0% of the tests

print("************")       
#Task 5. Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
with open("school_prompt.txt", "r") as sp_file:
    three = []
    sp_list = sp_file.readlines()
    for line in sp_list:
        word = line.split(" ")
        three.append(word[2])
print(three)
#You passed: 100.0% of the tests

print("************")
#Task 6. Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
with open("emotion_words.txt", "r") as emotion_file:
    emotions = []
    emotion_word = emotion_file.readlines()
    for emotion in emotion_word:
        word = emotion.split(" ")
        emotions.append(word[0])
print(emotions)
#You passed: 100.0% of the tests

print("************")
#Task 7. Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
with open("travel_plans.txt", "r") as travel_file:
    first_chars = travel_file.read(33)
print(first_chars)
#You passed: 100.0% of the tests

print("************")
#Task 8. Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
with open("school_prompt.txt", "r") as school_file:
    p_words = []
    word_list = school_file.read().split()
    for word in word_list:
        if "p" in word:
            p_words.append(word)
print(p_words)
#You passed: 100.0% of the tests
