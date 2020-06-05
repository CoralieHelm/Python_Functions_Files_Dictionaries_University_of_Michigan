#June 5
#13.2. Tuple Packing

#1. Create a tuple called practice that has four elements: ‘y’, ‘h’, ‘z’, and ‘x’.
practice = ('y','h','z','x')

print(practice)
print(">>>Task 1 Completed<<<")

#2. Create a tuple named tup1 that has three elements: ‘a’, ‘b’, and ‘c’.
tup1 = ('a','b','c')

print(tup1)
print(">>>Task 2 Completed<<<")

#3.Provided is a list of tuples. Create another list called t_check that contains the third element of every tuple.
lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]
t_check = []

for item in lst_tups:
    t_check.append(item[2])

print(t_check)
print(">>>Task 3 Completed<<<")

#4.  Below, we have provided a list of tuples. Write a for loop that saves the second element of each tuple into a list called seconds.

tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]
seconds = []

for item in tups:
    seconds.append(item[1])

print(seconds)
print(">>>Task 4 Completed<<<")
