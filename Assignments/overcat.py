"""
Name: Scott Schumacher
Email: scottmachershoe@yahoo.com
Assignment: fraction class
Due: 3 Oct 2016 @ 1:00 p.m.
"""




"""book = ['a', 'b', 3, 4, "joe"]
for banana in book:
	print(banana)

for i in range(len(book)):
	print (book[i])"""

dict ={'a': 1, 'b': 2, 'c': 3}

print(dict['a'])
"""for k in dict:
	print (k, 'corresponds to ', dict[k])

for key, value in dict.items():
	print(key, ':', value)"""


"""
def changemaker(cost, amtPaid):
	if (amtPaid < cost):
		print('you owe me more money.')
	elif(amtPaid == cost):
		print('no change required')
	else:
		change = amtPaid - cost
		#print(change)
		if change < 5:
			print('i will give you ', change, 'dollar bills.')
		elif change == 5:
			print('I will give you a five dollar bill.')
		elif 5 < change < 10:
			print('I will give you a five and ', (change - 5), 'dollar bills.')


changemaker(11, 20)
"""

"""
str = 'we dont need no education we dont need no thought control no we dont'
count = str.count('dont')
print(count)

"""


"""
class Student:
    def __init__(self, fname, lname, id, dob):
        self.first_name = fname
        self.last_name = lname
        self.id = id
        self.dob = dob
        
    def __str__(self):
    	return "(%s, %s, %d, %d)" %(self.first_name, self.last_name, self.id, self.dob)
        
newguy = Student('fred', 'flintstone', 776, 33)
print (Student.__str__(newguy))

"""

"""
Write a class called wordDictonary that represents an actual dictionary. Your 
class should contain the following methods:
loadDictionary :
     - reads a file that contains word: definition
     - a word may occur more than once (same word alternate definition)
     - you should be able to hold all definitions
updateDictionary:
     - a method that lets you add a word:definition to the class
findWord:
     - this method receives a word, and returns all definitions that correspond to it.
removeWord:
     - this method lets you remove a word from the dictionary.
"""
"""
class wordDictonary(object):
	def __init__(self):
		self.dict = {}
		
	def __str__(self):
		string = ''
		for k,v in self.dict.items():
			string += k + ":"
			for wd in v:
				string += "\n\t"
				string += ''.join(wd)
				
			string += "\n"
		return string
		
	def loadDictionary(self):
		path = r"C:\2143-OOP-Schumacher\assignments\scroll.txt"
		with open(path) as fiName:
			print(fiName.readline())
			print(fiName.readline())
			print(fiName.readline())
			print(fiName.readline())
		
		
	
	def updateDictionary(self,word,definition):
		if not word in self.dict:
			self.dict[word] = []
		self.dict[word].append(definition)
		
	def findWord(self,word):
		if word in self.dict:
			return self.dict[word]
		else:
			return None
	
	def removeWord(self,word):
		if word in self.dict:
			del self.dict[word]
			
			
wd = wordDictonary()
wd.updateDictionary('run','go fast')
wd.updateDictionary('run','move legs powerfully')
wd.updateDictionary('walk','go slow')
wd.updateDictionary('walk','not run')
wd.loadDictionary()



print(wd)

"""

"""
#Given the following example of how to overload an operator:

class Point:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

#Looks like an answer to another question!!! ;)
	def __str__(self):
		return "({0},{1})".format(self.x,self.y)
		# or
		# return "(%d , %d)" % (self.x,self.y)

	def __add__(self,other):
		x = self.x + other.x
		y = self.y + other.y
		return Point(x,y)

	def __compare__(self,other):
		if(self.x == other.x) and (self.y == other.y):
			print('They are equal')
		else:
			print('They are not')

#And it's usage:

p1 = Point(2,3)
p2 = Point(-1,2)
print(p1 + p2)
# prints: (1,5)
print(p1 == p2)

#Overload the equal operator to test for point equality.

"""

lst = [1, 2, 5, 7, 9]

def myfunk(worklist):
	elMin = min(worklist)
	elMax = max(worklist)
	elAve = sum(worklist)/len(worklist)
	print((elMin, elMax, elAve))

myfunk(lst)











