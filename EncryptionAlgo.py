'''
	class to encrypt large number
	
'''
import Encryptor

class EncryptionAlgo:

	def __init__(self, toEncrypt):
		self.encryptee = toEncrypt;
		self.encryption = []
		
		
	def execute(self):
		
		self.encryptor = Encryptor.Encryptor().getEncryptor();
		
		self.encryption = self.encryptionBegins();
		
	def encryptionBegins(self):
		
		encryp = ''
		encryptionLenght = 	len(self.encryptor);
		print(encryptionLenght)
		while(1):
			idx = self.encryptee%(encryptionLenght);
			print("remainder",idx)
			self.encryptee = int(self.encryptee/encryptionLenght);
			print("index of encryptor",self.encryptee)
			encryp = (self.encryptor[idx]) + encryp;
			if(self.encryptee<=0):
				break;
		
		return encryp;
		
	def getEncryption(self):
		return self.encryption;
	
		
	
		
	