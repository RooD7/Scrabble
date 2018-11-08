# def permutacao(s, i = 0):
# 	if i == len(s)-1:
# 		print(s)
# 	else:
# 		for j in range(i, len(s)):
# 		t = s
# 		s = s[j] + s[:j] + s[(j+1):]
# 		perm(s, i + 1)
# 		s = t

# permutacao('ABCD')

import Scrabble
class Player(object):
	def __init__(self):

	def jogar(self):
		pass

	def trocarLetra(self, pecasVelhas):
		novasPecas = []
		novasPecas = Scrabble.swapPeca(pecasVelhas)
		novasPecas.append()

	

