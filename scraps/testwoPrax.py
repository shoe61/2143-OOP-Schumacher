"""

    Create a class called "Color" that will store a tuple of (r,g,b).
    The tuple should be stored in a data member called color.
    The components of the color tuple should be stored in data members: red, green, blue as well
    Add a str method to print out the color class so it looks like: "(red: redVal, green: greenVal, blue: blueVal)"
    Here is some usage:

c1 = Color((255,0,0))
print(c1.red)
#prints: 255

c1.blue = 255
print(c1)
#prints: (red: 255, green: 0, blue: 255)

c1.color = (0,0,0)
print(c1)
#prints: (red: 0, green: 0, blue: 0)




Overload the addition operator so that we can add two colors. Adding colors is a pretty wierd experience, so we will create our own addition method. Basically we will average each color.

For example:

c1 = (255,255,255)
c2 = (0,0,0)
c3 = c1 + c2

print(c3)
#prints: (128,128,128)


"""
import math

class Color(object):
    def __init__(self, argeebee):
        self.red = argeebee[0]
        self.green = argeebee[1]
        self.blue = argeebee[2]
        self.color = (self.red, self.green, self.blue)    
    

    def __str__(self):
        return"red: %d, green: %d, blue: %d" %(self.red, self.green, self.blue)


    def __add__(self, annudder):
        red = int(self.red + annudder.red)
        green = int(self.green + annudder.green)
        blue = int(self.blue + annudder.blue)
        return Color((int(red/2), int(green/2), int(blue/2)))




c1 = Color((255, 0, 0))
print('c1.red: ', c1.red)
c1.blue = 100
print('c1 after changing blue to 100: ', c1)
c1.color = (0, 0, 0) # hold it! tuples are immutable.
print('tuples are immutable: ', c1)


c1 = Color((255,255,255))
c2 = Color((0,0,0))
c3 = c1 + c2
print('c3, being the addition of c1 and c2: ', c3)

"""
@Description: Gets an RGB color represented as a tuple, and converts it to a 
                gray scale equivalent based on chosen method.
@Methods:
    Lightness - as described above
    Average - as described above
    Luminosity - as described above
    Custom - as described above
    SetColor - Lets user change the color originally passed in.
"""

class Grayscale(Color):

    def __init__(self, someColor):
        self.red = someColor[0]
        self.green = someColor[1]
        self.blue = someColor[2]
        self.origColor = (self.red, self.green, self.blue)

    def Lightness(self):
        gra = ((min(self.red, self.green, self.blue) + max(self.red, self.green, self.blue))/2)
        return Color((gra, gra, gra))

    def Average(self):
        gra = (self.red + self.green + self.blue)/3
        return Color((gra, gra, gra))

    def Luminosity(self):
        ra = 0.21 * self.red
        ga = 0.72 * self.green
        ba = 0.07 * self.blue
        return Color((ra, ga, ba))

    def Custom(self, w1, w2, w3):
        ra = w1 * self.red
        ga = w2 * self.green
        ba = w3 * self.blue
        return Color((ra, ga, ba))


grayish = Grayscale((242, 128, 200))
c5 = grayish.Lightness()
c6 = grayish.Average()
c7 = grayish.Luminosity()
c8 = grayish.Custom(0.25, 0.69, 0.06)

print('grayish: ', grayish)
print('c5: ', c5)
print('c6: ', c6)
print('c7: ', c7)
print('c8: ', c8)

    