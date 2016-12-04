"""************************************************************************************************
Scott Schumacher, Program 3
main.py
This file will import or otherwise obtain an image. Main will use the methods in the ImageEd class
to perform various modifications.

************************************************************************************************"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import sys
import random
import urllib
from io import StringIO


"""************************************************************************************************
First, open a picture stored in this directory; display some info about it, and display it.

************************************************************************************************"""

pic = Image.open("klammer.jpg")
print (pic.size, pic.format, pic.mode)

"""************************************************************************************************
Then, create an ImageEd object. This object, franz, will call the various ImageEd methods to create
effects. 
************************************************************************************************"""
import imageEdit

#imageEdit.picShow(pic)
#imageEdit.picDescrip(pic)
#imageEdit.pixLister(pic)
#pic = pic.resize((270, 370), Image.ANTIALIAS)
#pic = imageEdit.checker(pic)

#pic = imageEdit.glassFilter(pic, 5)

#pic = imageEdit.hoFlipper(pic)

#pic = imageEdit.vFlipper(pic)

#pic = imageEdit.blur(pic, 2)

#pic = imageEdit.posterize(pic, 64)

#pic = imageEdit.solarize(pic, 190)

pic = imageEdit.warhol(pic, 64)
pic.show()

"""************************************************************************************************
************************************************************************************************"""

"""************************************************************************************************
************************************************************************************************"""
