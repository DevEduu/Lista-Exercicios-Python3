print(''*20)
print('{:=^30}'.format(' DESAFIO 26 '))
fr = str(input('Informe uma frase: ')).strip().lower()
print('Quantas vezes aparece  letra "A" é : {} vezes.'.format(fr.count('a')))
print('A primeira possição que aparece é posição {}.'.format(fr.find('a')+1))
print('A ultima posição é a: {}'.format(fr.rfind('a')+1))
