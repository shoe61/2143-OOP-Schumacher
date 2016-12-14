class MyList(object):

    def __init__(self, L = []):
        self.L = L

    def __add__(L1, L2):
        rezo = []
        
        for i in range(len(L1)):
            rezo.append(L1[i] + L2[i])
        return rezo





L1 = MyList([1,3,5])
L2 = MyList([2,4,6])
L3 = L1 + L2
print(L3)