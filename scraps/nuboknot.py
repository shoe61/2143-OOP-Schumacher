


"""
class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d,%d)' %(self.x, self.y)

pernt = Point(2,3)
print (pernt)



"""

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_old(self):
        return self.age >= 40

ish = Person('Scott', 55)
print(ish.is_old())