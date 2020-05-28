#May 28 2020
#Python Functions, Files, and Dictionaries - University of Michigan
#Week 1
#Reading a File

poem_ref = open("Invictus.txt", "r")

for poem in poem_ref:
    print(poem)

poem_ref.close()
                
