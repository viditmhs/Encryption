'''
	Unit test for encryption algrithm
'''

import EncryptionAlgo as E

def main():
	
	toEncrypt = 123456789987654321;
	e = E.EncryptionAlgo(toEncrypt);
	e.execute();
	print (e.getEncryption(), ' for ', toEncrypt );

if __name__ == '__main__':
	main();