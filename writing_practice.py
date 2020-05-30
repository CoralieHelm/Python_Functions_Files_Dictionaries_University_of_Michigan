#May 30 2020
#Writing to a file  practice

with open("generated_writing_file.txt", "w") as gw_file:
    gw_file.write("Today is saturday May 30th 2020. This file is intended to be used as a practice to write content to a file via python.")
    print("File has been created")
    print("**********************")

with open("generated_writing_file.txt", "a") as gw_file:
    gw_file.write("\n")
    gw_file.write("This was a popular exercise")
    gw_file.write("\n")
    print("File has been appended.")
    print(">>>>>>>>>>")
    
with open("generated_writing_file.txt", "a") as gw_file:
    gw_file.write("...and still is.")
    gw_file.write("\n")
    print("File has been appended.")
    print(">>>>>>>>>>")
