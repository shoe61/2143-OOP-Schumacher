"""
Name: Scott Schumacher
Email: scottmachershoe@yahoo.com
Assignment: Homework 1 - Lists and Dictionaries
Due: 19 Sep @ 1:00 p.m.
"""


""""A: What would Python print?"""

a = [1, 5, 4, 2, 3] 
print(a[0], a[-1])
# Prints: 13

a[4] = a[2] + a[-2]
print(a)
# Prints: [1,5,4,2,6]

print(len(a))
# Prints: 5

print(4 in a)
# Prints: True

a[1] = [a[1], a[0]]
print(a)
#replaces a[1] with a list containing a[1] and a[0]
# Prints: [1, [5, 1], 4, 2, 6]
"""****************************************************************************************"""


"""B. Write a function that removes all instances of an element from a list."""

def remove_all(rmv, lst):
    while rmv in lst:
        lst.remove(rmv)
           

b = [1, 4, 2, 4, 3, 4, 5]
remove_all(4, b)
print (b)
#prints [1, 2, 3, 5]
"""****************************************************************************************"""

"""C. Write a function that takes in two values, x and y, and a list, and adds as 
many y's to the end of the list as there are x's. Do not use the built-in function count."""

def for_x_append_y(x, y, lst):
    for el in lst:
        if el == x:
            lst.append(y)

c = [3, 5, 3, 2, 3]
for_x_append_y(3, 7, c)
print(c)
#prints [3, 5, 3, 2, 3, 7, 7, 7]
"""****************************************************************************************"""

"""D.  What would Python print?"""

a = [3, 1, 4, 2, 5, 3]
print(a[:4])
# Prints: [3, 1, 4, 2]

print(a)
# Prints: [3, 1, 4, 2, 5, 3]

print(a[1::2])
# Prints: [1, 2, 3]

print(a[:])
# Prints: [3, 1, 4, 2, 5, 3]

print(a[4:2])
# Prints: []

print(a[1:-2])
# Prints: [1, 4, 2]

print(a[::-1])
# Prints: [3, 5, 2, 4, 1, 3]
"""****************************************************************************************"""

"""E. Let's reverse Python lists in place, meaning mutate the passed in list itself, instead of 
returning a new list. We didn't discuss this in class directly, so feel free to use google. 
Why is the "in place" solution preferred?"""

import math

def reverse(lst):
    for el in range (0, math.ceil(len(lst)/2)):
        lst[el], lst[len(lst)-1-el] = lst[len(lst)-1-el], lst[el]

e = [1, 2, 3, 4, 5, 6, 7]
reverse(e)
print(e)
#prints [7, 6, 5, 4, 3, 2, 1]
"""****************************************************************************************"""

