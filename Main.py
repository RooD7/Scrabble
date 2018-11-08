import Scrabble

class Main(object):

	scrb = Scrabble.Scrabble()
	s = scrb.getSaco()
	# print(len(s))
	# print(s)
	# print('Pesquisando...abacate:')
	# scrb.pesquisarDic(['abacate'])
	# print('Pesquisando...janela:')
	# scrb.pesquisarDic(['janela'])
	# print('Pesquisando...zebra:')
	# scrb.pesquisarDic(['zebrad'])

	print('Pecas P1:')
	print(scrb.getPecasP1())
	# letra = input('Trocar Pecas P1:')
	# scrb.trocarLetras('P1',[letra])
	# print(scrb.getPecasP1())
	perm = scrb.geradorPalavras('P1')
	# print(perm)
	palavras = scrb.pesquisarDic(perm)
	print(palavras)


	print('\nPecas P2:')
	print(scrb.getPecasP2())
	# letra = input('Trocar Pecas P2:')
	# scrb.trocarLetras('P2',[letra])
	# print(scrb.getPecasP2())
	perm = scrb.geradorPalavras('P2')
	# print(perm)
	palavras = scrb.pesquisarDic(perm)
	print(palavras)