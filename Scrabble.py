import Start
from patricia import trie
import random
from datetime import datetime

class Scrabble(object):
	"""Estrutura do Scrabble"""

	def __init__(self):		
		random.seed(datetime.now())
		self.st = Start.Start()
		self.tabuleiro = self.st.startTabuleiro()
		self.saco = self.st.startSaco()
		self.dicionario = self.st.startDicionario()
		self.pecas_P1 = self.startPecas()
		self.pecas_P2 = self.startPecas()
		self.permuta = []
		self.palavrasVD = []

	def startPecas(self):
		pecas = []
		for x in range(0,7):
			p = random.choice(self.saco)
			pecas.append(p)
			self.saco.remove(p)
		return pecas

	def geradorPalavras(self, player):
		letras = ''
		if player == 'P1':
			for p in self.pecas_P1:
				letras += p[0].lower()
		elif player == 'P2':
			for p in self.pecas_P2:
				letras += p[0].lower()

		self.permuta = []
		for i in range(2,len(letras)):
			# print('letras')
			# print(letras)
			# print(letras[:i])
			# print(len(letras[:i]))
			self.permutacao(letras[:i])
		return self.permuta


	def permutacao(self, s, i = 0):
		if i == len(s)-1:
			if not s in self.permuta:
				self.permuta.append(s)
		else:
			for j in range(i, len(s)):
				t = s
				s = s[j] + s[:j] + s[(j+1):]
				self.permutacao(s, i + 1)
				s = t

	def pesquisarDic(self, palavras):
		self.palavrasVD = []
		for p in palavras:
			# if self.dicionario.isPrefix(p):
			# 	print('Encontrado!')
			# 	print(sorted(self.dicionario.iter(p)))
			if p in self.dicionario:
				self.palavrasVD.append(p)
				# print('Encontrado!->'+str(p))
			else:
				pass
				# print('Não Encontrado!')
		return self.palavrasVD

	def getNovaPeca(self):
		p = random.choice(self.saco)
		self.saco.remove(p)
		return p

	def searchPeca(self, letra):
		for p in self.saco:
			if p[0] == letra:
				print('Encontrou: ')
				print(p)
				return p
		return None

	def trocarLetras(self, player, pecas):
		pecasVelhas = []
		for p in pecas:
			peca = self.searchPeca(p)
			if peca != None:
				pecasVelhas.append(peca)
		
		if player == 'P1':
			# self.pecas_P1.extend(novasPecas)
			self.pecas_P1 = self.swapPecas(self.pecas_P1, pecasVelhas)
		elif player == 'P2':
			self.pecas_P2 = self.swapPecas(self.pecas_P2, pecasVelhas)

	def swapPecas(self, minhas, velhas):
		novas = []
		# novas pedras
		for v in velhas:
			# sorteia pedras novas
			p = random.choice(self.saco)
			novas.append(p)
			# remove pedras velhas
			minhas.remove(v)
		# adiciona as novas pedras
		minhas.extend(novas)
		# retorna pedras velhas pro saco
		for v in velhas:
			self.saco.append(v)
		return minhas

	def getTabuleiro(self):
		return self.tabuleiro

	def getSaco(self):
		return self.saco

	def getPecasP1(self):
		return self.pecas_P1

	def getPecasP2(self):
		return self.pecas_P2


		