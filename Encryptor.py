'''
	To encrypt a generate encryptor array based on an ecryption file 
'''

class Encryptor:
	
	def __init__(self):
		self.encryptor = []
		
	def execute(self):
		
		self.readEncryptionFile();
		
	def readEncryptionFile(self):
		
		filePath = self.getEncryptionFileLocation()
		_file = open(filePath, 'r');
		
		for line in _file:
			if(line[0]=='#'):
				print('LOG: ' + line )
			else:
				self.encryptor.append(line);
		
	def getEncryptionFileLocation(self):
		# this need to move to some properties files		
		return "encryption.txt"
	
	def getEncryptor(self):
		self.execute();
		return self.encryptor[0];

	