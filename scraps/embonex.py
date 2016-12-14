class Color(object):

    def __init__(self, r=0, g=0, b=0):
        if type(r) == tuple:
            self.r, self.g, self.b = (r)
        else:
            self.r = r
            self.g = g
            self.b = b

    def __str__(self):
        return "(%d, %d,%d)" %(self.r, self.g, self.b)

red = Color((255,0,0))
print(red)