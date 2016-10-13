"""
Name: Scott Schumacher
Email: scottmachershoe@yahoo.com
Assignment: fraction class
Due: 3 Oct 2016 @ 1:00 p.m.
"""


"""
@ Name: ShiftCipher
@ Description: Simple class to do a shift cipher
"""
class ShiftCipher(object):
	
	"""
	@ Name: __init__
	@ Description: Constructor
	@ Params: None
	"""
	def __init__(self):
		
		self.plainText = None
		self.cipherText = None
		self.cleanText = None
		self.shift = 3

	"""
	@ Name: __init__
	@ Description: Constructor
	@ Params: None
	"""
	def __str__(self):
		return "plainText: %s\ncipherText: %s\ncleanText: %s\nshift: %d\n" % (self.plainText,self.cipherText,self.cleanText,self.shift)
	
	"""
	@ Name: promptUserMessage
	@ Description: Prompts user for message from standard in
	@ Params: None
	"""
	def promptUserMessage(self):
		temp = input("Message: ")
		self.setMessage(temp)

	"""
	@ Name: setMessage
	@ Description: sets plaintext and then cleans and calls encrypt.
	@ Params:	message {string}: String message
	     		encrypted {bool}: False = plaintext True=ciphertext
	"""
	def setMessage(self,message,encrypted=False):
		if(not encrypted):
			self.plainText = message
			self.cleanData()
			self.__encrypt()
		else:
			self.cipherText = message
			self.__decrypt()

	"""
	@ Name: getCipherText
	@ Description: gets cipher text
	@ Params: None
	"""	
	def getCipherText(self):
		return self.cipherText

	"""
	@ Name: getPlainText
	@ Description: gets plain text
	@ Params: None
	"""		
	def getPlainText(self):
		return self.plainText

	"""
	@ Name: setShift
	@ Description: sets this.shift
	@ Params: shift
	"""
	def setShift(self,shift):
		self.shift = shift

	"""
	@ Name: getShift
	@ Description: gets shift
	@ Params: None
	"""	
	def getShift(self):
		return self.shift

	"""
	@ Name: cleanData
	@ Description: 	removes all but alphanumeric characters
	@				converts all alpha to uppercase
	@ Params: None
	"""		
	def cleanData(self):
		self.cleanText = ''
		for letter in self.plainText:
			# ignore spaces
			if ord(letter) == 32:
				continue
			# ignore characters where ord < 48, floor numerals
			if ord(letter) < 48:
				continue
			# ignore charactes between ceiling numerals and floor letters
			if 57 < ord(letter) < 65:
				continue
			if 90 < ord(letter) < 97:
				continue
			# change all lowercase letters to uppercase
			if 123 > ord(letter) > 96:
				self.cleanText += chr(ord(letter)-32)
			else:
				self.cleanText += letter

	"""
	@ Name: __encrypt
	@ Description: 	encrypts clean text
	@ Params: None
	"""	
	def __encrypt(self):
		self.cipherText = ''
		if(not self.cleanText):
			return
		for letter in self.cleanText:
			""" Changed the adjustment from 65 to 48 to avoid negative numbers; range expanded from 0-26 to 0-43;
			This eliminates the possibility of a letter and number encrypting to the same value. Sometimes the cipherText
			will have characters other than alphanumeric, but clean and plain texts are strictly alphanumeric. """
			self.cipherText += chr((((ord(letter)-48) + self.shift) % 43)+48)
		    
	"""
	@ Name: __decrypt
	@ Description: 	decrypts cipher text...very simple!
	@				reverses the encryption process: subtracts shift and reverses
	@				modulo operation by adding 43 until character is within range
	@				of uppercase alphanumerics
	@ Params: None
	"""	
	def __decrypt(self):
		self.plainText = ''
		if(not self.cipherText):
			return
		for letter in self.cipherText:
			ltr = ord(letter) - self.shift
			while ltr < 48:
				ltr += 43 
			self.plainText += chr(ltr)
			


"""
Only run this if we call this file directly:
"""
if __name__=='__main__':

    alice = ShiftCipher()
    alice.promptUserMessage()
    print(alice)


    bob = ShiftCipher()
    bob.setMessage(alice.getCipherText(),True)
   


    
print('bob: \n' , bob)