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
""" F. Write a function that rotates the elements of a list to the right by k. Elements should not
 ”fall off”; they should wrap around the beginning of the list. rotate should return a new list. 
 To make a list of n 0's,you can do this: [0] * n """

def rotate(lst, k):
    g = []
    for i in range(len(lst)):
        i -= k
        g.insert(len(g), lst[i])
    print(lst)
    print(g)

f = [1, 2, 3, 4, 5, 6]
rotate(f, 3)
"""prints:
    [1, 2, 3, 4, 5, 6]
    [4, 5, 6, 1, 2, 3]
"""

"""****************************************************************************************"""
"""H: Continuing from above, what would Python print?"""

print('colin kaepernick' in superbowls)
#Prints: False

print(len(superbowls))
#Prints: 4         (Originally 3,  Payton Manning added = 4)

print(superbowls['peyton manning'] == superbowls['joe montana'])
#Prints: False

superbowls[('eli manning', 'giants')] = 2
print(superbowls)
#Prints: {'peyton manning': 1, ('eli manning', 'giants'): 2, 'tom brady': 3, 'joe flacco': 1, 'joe montana': 4}

superbowls[3] = 'cat'
print(superbowls)
#Prints: {3: 'cat', 'peyton manning': 1, 'joe flacco': 1, 'joe montana': 4, 'tom brady': 3, ('eli manning', 'giants'): 2}


superbowls[('eli manning', 'giants')] =  superbowls['joe montana'] + superbowls['peyton manning']
print(superbowls)
#Prints: {3: 'cat', 'peyton manning': 1, 'joe flacco': 1, 'joe montana': 4, 'tom brady': 3, ('eli manning', 'giants'): 5}

superbowls[['steelers', '49ers']] = 11
print(superbowls)
#Prints: TypeError: unhashable type: 'list'

"""****************************************************************************************"""

"""I: Given a dictionary replace all occurrences of x as the value with y."""

def replace(d, x, y):
    for k in d.keys():
        if d[k] == x:
            d[k] = y
    print(d)

dict = {'bob': 3, 'fred': 7, 'wilma': 8, 'ginger': 4, 'maryann': 9}
replace(dict, 9, 'nine')
#prints: {'fred': 7, 'ginger': 4, 'maryann': 'nine', 'wilma': 8, 'bob': 3}

"""****************************************************************************************"""
"""J: Given a (non-nested) dictionary delete all occurences of a value. You cannot delete 
items in a dictionary as you are iterating through it."""

def removIt(d, rmv):
    d = {k:v for k, v in d.items() if not v == rmv}
    print(d)

d = {1:2, 'underdog': 'sweet polly purebred', 2:3, 3:2, 4:5, 7:2, 'boris': 'natasha', 'tobor': 2}
removIt(d, 2)

#prints: {'underdog': 'sweet polly purebred', 2: 3, 4: 5, 'boris': 'natasha'}
