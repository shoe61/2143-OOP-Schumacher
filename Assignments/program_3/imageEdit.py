"""************************************************************************************************
Scott Schumacher, Program 3
imageEdit.py

This file contains image filter methods; it's used by main to perform operations on existing images:

    glass_effect
    flip
    blur
    posterize
    solarize
    warhol

************************************************************************************************"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import sys
import random
import urllib
from io import StringIO

"""============================================================================================

method checker

traverse the image; for all pixels where x and y are multiples of 2, color the pixel black

Params: img

============================================================================================="""

def checker(img):
    width = img.size[0]
    height = img.size[1]
    for x in range(width):
        for y in range(height):
            if x % 2 == 0 and y % 2 == 0:
                img.putpixel((x,y), (255, 255, 255))
    return img

"""============================================================================================

method glassFilter

traverse the image and substitute for each pixel another random pixel within diz of the current
pixel. Using if statements allows the effect to extend all the way to the borders of the image.

Params: img and diz, the distance within which a random pixel can be selected

============================================================================================="""

def glassFilter(img, diz):

    width = img.size[0]
    height = img.size[1]

    for x in range(width):
        
        for y in range(height):
            dx = random.randint(0, diz)
            getx = x + dx
            if getx > width -1:
                getx = x - dx
            dy = random.randint(0, diz)
            gety = y + dx
            if gety > height - 1:
                gety = y - dx
            px = img.getpixel((getx, gety))
            r = px[0]
            g = px[1]
            b = px[2]
            img.putpixel((x,y), (r,g,b))

    return img

"""============================================================================================

method hoFlipper (horizontal flipper)

traverse HALF the image, substituting a column of pixels for its mirror counterpart

Params: img

============================================================================================="""

def hoFlipper(img):

    width = img.size[0]
    height = img.size[1]

    for y in range(height):
        #print("x: ", x, " opp: ", opposite)
        for x in range(int(width/2)):
            opposite = (width -1) - x
            xxl = img.getpixel((x,y))
            rx = xxl[0]
            rg = xxl[1]
            rb = xxl[2]
            opxl = img.getpixel((opposite, y))
            rop = opxl[0]
            gop = opxl[1]
            bop = opxl[2]
            img.putpixel((x,y),(rop, gop, bop))
            img.putpixel((opposite,y),(rx, rg, rb))
    return img

"""============================================================================================

method vFlipper (vertical flipper)

traverse HALF the image, substituting a row of pixels for its mirror counterpart

Params: img

============================================================================================="""

        
def vFlipper(img):

    width = img.size[0]
    height = img.size[1]

    for x in range(width):
        
        for y in range(int(height/2)):
            opposite = (height -1) - y
            yxl = img.getpixel((x,y))
            rx = yxl[0]
            rg = yxl[1]
            rb = yxl[2]
            opxl = img.getpixel((x, opposite))
            rop = opxl[0]
            gop = opxl[1]
            bop = opxl[2]
            img.putpixel((x,y),(rop, gop, bop))
            img.putpixel((x, opposite),(rx, rg, rb))
    return img

"""============================================================================================
method blur

a kernel that extends r pixels in all directions about a given pixel averages all the rgb values
and writes them to the subject pixel.

To account for borders, the iteration will begin r pixels from any boundary

Parameters: img, the image to be modified, and r, the user-settable blur range

============================================================================================="""


def blur(img, rg):
    
    width = img.size[0]
    height = img.size[1]
    zerg = 2*rg +1
    zerg2 = zerg*zerg
    
    # the kernel traverses an area within the image with a border r pixels wide
    for x in range(rg, width-(rg + 1)):
        for y in range(rg, height-(rg + 1)):
            # average the r, g, b values of all the pixels within the box defined by (x +- r, y+-r)
            # that means traversing a box 2r+1 long and wide, summing the values, and dividing by
            # (2r +1) squared
            r = 0
            g = 0
            b = 0
            for w in range(-rg, rg):
                for h in range(-rg, rg):
                    pxl = img.getpixel((x + rg, y + rg))
                    r = r + pxl[0]
                    g = g + pxl[1]
                    b = b + pxl[2]
            r = int(r /zerg2)
            g = int(g /zerg2)
            b = int(b /zerg2)

            img.putpixel((x,y),(r, g, b))
    return img
    
"""============================================================================================

method posterize

Parameters: img file and snap, which is the value by which all r, g, b colors will be modded by.

Traverse the image, performing the snap operation of each of the three color values.

============================================================================================="""

def posterize(img, snap):

    width = img.size[0]
    height = img.size[1]

    # traverse the image 
    for x in range (width):
        for y in range(height):
            #read the pixel and extract the values
            (r,g,b) = img.getpixel((x,y))
            # round each color up or down to the nearest snap ValueError
            
            rr = r
            m = rr % snap
            if m < (snap // 2):
                rr -= m
            else:
                rr += (snap - m)
            
            gg = g
            n = gg % snap
            if n < (snap // 2):
                gg -= n
            else:
                gg += (snap - n)

            bb = b
            o = bb % snap
            if o < (snap // 2):
                bb-= o
            else:
                bb += (snap - o)  

            img.putpixel((x, y), (rr, gg, bb))

    return img

"""============================================================================================

method solarize

negates the r, g, b values of each pixel if they exceed a user-defined threshold

paramters: img, threshold

============================================================================================="""   

def solarize(img, lim):

    width, height = img.size

    for x in range(width):
        for y in range(height):
            (r, g, b) = img.getpixel((x, y)) 

            rr = r
            if rr > lim:
                rr = 255 - rr

            gg = g
            if gg > lim:
                gg = 255 - gg
            
            bb = b
            if bb > lim:
                bb = 255 - bb

            img. putpixel((x,y), (rr, gg, bb))

    return img

"""============================================================================================
"In the future, everyone will be famous for fifteen minutes." --Andy Warhol

method warhol: converts image to grayscale, then posterizes; for each interval created, uses a 
single list- defined color provided by method (not user defined)

parameters: img and snap value.

============================================================================================="""

def warhol(img, snap):

    width, height = img.size

    # number of regions = 255 / snap
    regions = int(255/snap)
    

    # color list:
    colors =[(255,0,0), (0, 255, 0), (0, 0, 255), (128, 128, 0), (128, 0, 128)]

    # set up the traverse loop
    for x in range(width):
        for y in range(height):
            # get grayscale Image
            r, g, b = img.getpixel((x, y))
            gra = int((r+g+b)/3)
            img.putpixel((x,y), (gra, gra, gra))
            #posterize one channel (they're all the same!)
            rr = gra
            m = rr % snap
            if m < (snap // 2):
                rr -= m
            else:
                rr += (snap - m)

            # now, evaluate rr to determine the color to be used for the pixel
            for i in range(1, regions + 1):
               
                if rr < (i * 255) / regions and rr > (i - 1) * 255/ regions:
                    img.putpixel((x, y), (colors[i % 5 -1]))
                    
    return img

    