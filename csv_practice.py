# May 30th 2020
# Practising reading and writing from and to csv files via Python

#Practice 1:
#Opening and reading a simple csv file from yahoo finance.
with open("GSPC.csv", "r") as spc_file:
    print(spc_file.read())
#Notice that it is parsed as a string.

#Note: Python Functions, Files, and Dictionaries Week 1 does not introduce us yet
#to ths csv module. The following exercise is based on "CodeAcademy" - "Learning Python: Files"
import csv

with open("updatedProduceSales.csv", "r") as ups_file:
    ups_csv = csv.DictReader(ups_file)
    #DictReader converts the cvs lines to a dictionary
    for row in ups_csv:
        print(row)
