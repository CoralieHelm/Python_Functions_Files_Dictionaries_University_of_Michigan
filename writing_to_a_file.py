#May 28 2020

#Python Functions, Files, and Dictionaries - University of Michigan
#Week 1
#Reading from a file

file_obj = open("squares.txt", "w")
for number in  range(13):
    square = number * number
    print(square)
    file_obj.write(str(square))
    file_obj.write("\n")
file_obj.close()


new_file_obj = open("squares.txt", "r")
print(new_file_obj.read()[:10])
