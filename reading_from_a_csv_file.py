#May 28 2020

#Python Functions, Files, and Dictionaries - University of Michigan
#Week 1
#Reading from a csv file

with open("ABIO.csv", "r") as file_csv:
    lines = file_csv.readlines()
    header = lines[0]
    field_names = header.strip().split(" , ")
    print(field_names)
    for row in lines[1:]:
        vals = row.strip().split(" , ")
        print(vals)
