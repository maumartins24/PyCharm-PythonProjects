frase = str(input('Digite uma frase: ')).strip()
fraseL = frase.lower()
print('A letra A aparece {} vezes na frase '.format(fraseL.count('a')))
print('A primeira letra A aparece na posição {} '.format(fraseL.find('a')))