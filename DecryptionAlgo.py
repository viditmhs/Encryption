'''
	class to encrypt large number
	
'''
import Encryptor

class DecryptionAlgo:

	def __init__(self, toDecrypt):
		self.decryptee = toDecrypt;
		self.decryption = []
		
		
	def execute(self):
		
		self.decryptor = Encryptor.Encryptor().getEncryptor();
		
		self.decryption = self.decryptionBegins();
		
	def decryptionBegins(self):
		
		decryp = ''
		decryptionLenght = 	len(self.decryptor);
		value = 0;
		print(self.decryptee)
		for i in range(len(self.decryptee)):
			loc = self.decryptee[-1-i];
			print("encryted:", loc);
			idx = self.decryptor.find(loc);
			print("index:", idx)
			value = value + idx*pow(decryptionLenght,i);
			
		return value;
		
	def getDecryption(self):
		return self.decryption;