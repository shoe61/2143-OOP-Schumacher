class fraction(object):
    def __init__(self,w=None,n=None,d=None):
        self.whole = w        
        self.numerator = n
        self.denominator = d

    def __str__(self):
        return "%s-%s/%s" % (self.whole , self.numerator , self.denominator)

    def whole(self,w):
        self.whole = w
    
    def numerator(self,n):
        self.numerator = n 

    def denominator(self,d):
        self.denominator = d
		
    def __mul__(self,rhs):
        x = self.numerator * rhs.numerator
        y = self.denominator * rhs.denominator
        return fraction(x,y)	
		
    def __add__(self, rhs):
        w= (self.numerator * rhs.denominator + rhs.numerator * self.denominator) // (self.denominator * rhs.denominator)
        x= (self.numerator * rhs.denominator + rhs.numerator * self.denominator) % (rhs.denominator * self.denominator) 
        y= self.denominator * rhs.denominator
        return fraction(w,x,y)  

if __name__ == '__main__':
    a = fraction(0,3,5)
    b = fraction(0,3,4)
    c = a + b
    print (a, '+',  b, '=', c)
