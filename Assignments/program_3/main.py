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
effects. Import ImageEdit:
************************************************************************************************"""

import imageEdit

"""************************************************************************************************
Funtions below will modify the existing image; un- comment the function you want to demo, and run 
from GitBash. You may combine functions- but be prepared to wait, especially for blur. Functions are 
described in imageEdit.

************************************************************************************************"""


#pic = imageEdit.checker(pic)

#pic = imageEdit.glassFilter(pic, 5)

#pic = imageEdit.hoFlipper(pic)

#pic = imageEdit.vFlipper(pic)

# blur takes a long time...a LONG time.
#pic = imageEdit.blur(pic, 4)

pic = imageEdit.posterize(pic, 64)

#pic = imageEdit.solarize(pic, 190)

#pic = imageEdit.warhol(pic, 64)

pic.show()


"""************************************************************************************************
************************************************************************************************"""

"""************************************************************************************************
************************************************************************************************"""
