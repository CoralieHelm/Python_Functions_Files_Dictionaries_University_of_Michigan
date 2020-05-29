#May 29 2020
#Python Functions, Files, and Dictionaries - University of Michigan
#Week 1
#Writing to a csv file


cs_books = [("Types and Programming Languages", 2002, "Benjamin C. Pierce"),
             ("Code: The Hidden Language of Computer Hardware and Software", 30, "Charles Petzold"),
             ("Clean Code: A Handbook of Agile Software Craftsmanship", 2008, "Robert C. Martin"),
             ("Code Complete: A Practical Handbook of Software Construction", 2004, "Steve McConnell")]

outfile = open("computer_science_books.csv", "w")
# output the header row
outfile.write('Title,Year,Author')
outfile.write('\n')
# output each of the rows:
for book in cs_books:
    row_string = '{},{},{}'.format(cs_books[0], cs_books[1], cs_books[2])
    outfile.write('\n')
    outfile.write(row_string)
    outfile.write('\n')
print("File Creation Completed")


olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics.csv", "w")
# output the header row
outfile.write('Name,Age,Sport')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
print("Reduced Olympics File has been successfully created")
outfile.close()
