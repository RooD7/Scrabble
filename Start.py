import numpy as np
from patricia import trie

class Start(object):
	
	# @staticmethod
	def startTabuleiro(self):
		x = np.zeros(shape=(15, 15))
		return x

	# @staticmethod
	def startSaco(self):
		saco = []
		for x in range(0,3):
			saco.append(('',0))
			saco.append(('B',3))
		for x in range(0,14):
			saco.append(('A',1))
		for x in range(0,11):
			saco.append(('E',1))
		for x in range(0,10):
			saco.append(('I',1))
			saco.append(('O',1))
		for x in range(0,8):
			saco.append(('S',1))
		for x in range(0,7):
			saco.append(('U',1))
		for x in range(0,6):
			saco.append(('M',1))
			saco.append(('R',1))
		for x in range(0,5):
			saco.append(('T',1))
			saco.append(('D',2))
			saco.append(('L',2))
		for x in range(0,4):
			saco.append(('C',2))
			saco.append(('P',2))
			saco.append(('N',3))
		for x in range(0,2):
			saco.append(('Ç',3))
			saco.append(('F',4))
			saco.append(('G',4))
			saco.append(('H',4))
			saco.append(('V',4))
			saco.append(('J',5))
		saco.append(('Q',6))
		saco.append(('X',8))
		saco.append(('Z',8))

		return saco
	
	# @staticmethod
	def startDicionario(self):
		T = trie('root')
		try:
			file = open('wordlist.txt','r')
			for l in file:
				l = l.rstrip('\n')
				T[l] = l
			return T
		except Exception as e:
			raise e


