class fraction(object):

    def __init__(self,wh=None,n=None,d=None):
        if wh:
            self.whole = wh
        else:
            self.whole = 0.0
        self.numerator = n + self.whole * d
        self.denominator = d
        self.reduce()
    
    def reduce(self):
        thegcd = self.gcd(self.numerator,self.denominator)
        self.numerator =int(self.numerator / thegcd)
        self.denominator = int (self.denominator / thegcd)
        if self.numerator > self.denominator:
            self.whole = int(self.numerator / self.denominator)
            self.numerator %= self.denominator
            
    def gcd(self, a, numerator):
        
        while numerator:      
            a, numerator = numerator, a % numerator
        return a
        
    def __str__(self):
        if self.whole  > 0:
            return "%d    %d / %d" % (self.whole,self.numerator,self.denominator)
        else: 
            return "%d / %d" %(self.numerator,self.denominator)

    def __mul__(self,rhs):
        numerator = (self.numerator + int(self.denominator * self.whole))  * (rhs.numerator + int(rhs.denominator * rhs.whole))
        denominator = self.denominator * rhs.denominator
        return fraction(0,numerator,denominator)
    
    def __add__(self,rhs):
        denominator = int(self.denominator * rhs.denominator)
        numerator = int((self.numerator + int(self.denominator * self.whole)) * rhs.denominator) + int((rhs.numerator + int(rhs.denominator * rhs.whole)) * self.denominator)
        if(numerator == denominator):
            return 1
        else:
            return fraction(0, numerator,denominator)

if __name__ == '__main__':

    a = fraction(1,1,2)
    b = fraction(0,4,5)
    c = a*b
    d = a + b
    print('fraction a = ',a)
    print('fraction b = ',b)
    print('a times b = ',c)
    print('a plus b = ',d)






