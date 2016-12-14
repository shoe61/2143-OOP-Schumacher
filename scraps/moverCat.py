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


"""
@Class:         Cat
@Description:   extends Pet class to describe a cat
@Methods:       talk- gives cat distinct voice 
                lose_life- decrements the cat's number of lives; kills cat at zero.
"""  

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner)
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