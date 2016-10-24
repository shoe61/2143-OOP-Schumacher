###Scott Schumacher
###homework-04.md

'''python

#************************************************************

"""QUESTION 1: 1. Implement the Cat class by inheriting from the Pet class. Make sure to use superclass methods 
wherever possible. In addition, add a lose_life method to the Cat class."""



class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True # It’s alive!!!
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print('...')

class Dog(Pet):
    def __init__(self, name, owner, color):
        Pet.__init__(self, name, owner)
        self.color = color
    def talk(self):
        print('woof!')



class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.livesRemaining = lives
        print(self.name, 'is a cat.')

    def talk(self):
        """A cat says meow! when asked to talk."""
        print('meow!')
        
    def lose_life(self):
        if self.livesRemaining > 1:
            self.livesRemaining -= 1
            if self.livesRemaining == 0:
                self.is_alive = False    

# Create a cat
Spike = Cat('Spike', 'Scott', 9)
# Feed the cat
Spike.eat('mackerel')
# Check life balance
print(Spike.name, ' has ', Spike.livesRemaining, ' lives remaining.')
# Cat was playing in traffic
print('Spike was playing in traffic.')
Spike.lose_life()
# Recheck Balance
print(Spike.name, ' has ', Spike.livesRemaining, ' lives remaining.')
# Cat was out in pasture after dark; watch out for coyotes!
print('Coyotes love to eat cats.')
Spike.lose_life()
# New balance
print(Spike.name, ' has ', Spike.livesRemaining, ' lives remaining.')




#************************************************************

# QUESTION 2:

class Foo(object):
    def __init__(self, a):
        self.a = a
    def garply(self):
        return self.baz(self.a)

class Bar(Foo):
    a = 1
    def baz(self, val):
        return val

f = Foo(4)
b = Bar(3)
print(f.a)
# prints 4

print(b.a)
# prints 3

#COMMENTED OUT BELOW LINE SO DOCUMENT WILL RUN FOR GRADING.
#print( f.garply())
# prints an error message: AttributeError: 'Foo' object has no attribute 'baz'
print('AttributeError: Foo object has no attribute baz')

print(b.garply())
# prints 3

b.a = 9
print(b.garply())
# prints 9

f.baz = lambda val: val * val
print(f.garply())
# prints 16

'''




 
