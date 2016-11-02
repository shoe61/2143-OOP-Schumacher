class BinSearch(object):

    def __init__(self, somelist):
        self.workList = []
        self.worklist = sorted(somelist)
       

    def FindIt(self, target):
        f = 0
        l = len(self.worklist) 
        found = False

        while not found:
            m = (f + l)//2
                       
            if f > l:
                return None
            
            elif self.worklist[m] == target:
                found = True
                return m
            
            else:
                if self.worklist[m] > target:
                    l = m -1
                else:
                    f = m + 1

        

exlist = BinSearch([1,3,5,7,9,11,13,15,17,19])
print('finding in list: ', exlist.FindIt(1))

        
