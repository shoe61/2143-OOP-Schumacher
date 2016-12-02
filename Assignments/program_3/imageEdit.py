"""************************************************************************************************
Scott Schumacher, Program 3
imageEdit.py

This file contains the ImageEd class; it is used by main to perform operations on existing images:

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

def picShow(img):
    img.show()

def picDescrip(img):
    print("The picture is ", img.size[0], "pixels wide and ", img.size[1], "pixels high.")

def pixLister(img):
    pixList = list(img.getdata())
    print(pixList)

def checker(img):
    width = img.size[0]
    height = img.size[1]
    for x in range(width):
        for y in range(height):
            if x % 2 == 0 and y % 2:
                img.putpixel((x,y), (255, 255, 255))
    return img

    """============================================================================================





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





    
 

    