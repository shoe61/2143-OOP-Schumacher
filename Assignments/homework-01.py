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

"""B Write a function that removes all instances of an element from a list."""

def remove_all(rmv, lst):
    for el in lst:
        if el == rmv:
            a.remove(rmv)

remove_all(4,a)
print (a)



