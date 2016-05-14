'''
	Unit test for encryption algrithm
'''

import EncryptionAlgo as E
import DecryptionAlgo as D

def main():
	
	toEncrypt = pow(63,10);
	e = E.EncryptionAlgo(toEncrypt);
	e.execute();
	print (e.getEncryption(), ' for ', toEncrypt );
	
	d = D.DecryptionAlgo(e.getEncryption());
	d.execute();
	print (d.getDecryption(), ' for ', toEncrypt );

if __name__ == '__main__':
	main();