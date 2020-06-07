#June 6 2020
#14.2. The while Statement

#Check your
#moreiter-2-1: True or False: You can rewrite any for-loop as a while-loop
#A. True

#moreiter-2-2: The following code contains an infinite loop. Which is the best explanation for why the loop does not terminate?
""""
n = 10
answer = 1
while ( n > 0 ):
  answer = answer + n
  n = n + 1
print(answer)"""
#A. n starts at 10 and is incremented by 1 each time through the loop, so it will always be positive

# THE Code above has been corrected to resolve the infinite Loop
n = 1
answer = 1
while ( n < 10 ):
  answer = answer + n
  n = n + 1
print("The answer is:", answer)


#moreiter-2-3: Which type of loop can be used to perform the following iteration: You choose a positive integer at random and then print the numbers from 1 up to and including the selected integer.
#A. a for-loop or a while-loop
print("<<<Task 1>>>")
#Task 1. Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number, append the counter to a list called eve_nums.
start = 0
eve_nums = []

while start <= 15:
    if start % 2 == 0:
        eve_nums.append(start)
    start += 1
print(eve_nums)
print("**********")

print("<<<Task 2>>>")
#Task 2. Below, we’ve provided a for loop that sums all the elements of list1. Write code that accomplishes the same task, but instead uses a while loop. Assign the accumulator variable to the name accum.

list1 = [8, 3, 4, 5, 6, 7, 9]

tot = 0
for elem in list1:
    tot = tot + elem

index = 0
accum = 0

while index < len(list1):
    accum = accum + list1[index]
    index = index + 1
print(index, accum)
print("**********")

print("<<<Task 3>>>")
#Task 3. Write a function called stop_at_four that iterates through a list of numbers. Using a while loop, append each number to a new list until the number 4 appears. The function should return the new list.

def stop_at_four(list):
    new_list = []
    index_counter = 0

    while index_counter < len(list) and list[index_counter] != 4:
        new_list.append(list[index_counter])
        index_counter = index_counter + 1
    return new_list

list1 = [2,5,6,78,2,4,5]
print(stop_at_four(list1))  
print("**********")
