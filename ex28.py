from random import randint
#escreva um programa que faça o computador pensar em um numero
# inteiro entre 0 w 5 e peça para o usuario tentar
# descobrir qual foi o número escolhido pelo computador.
#o programa devera escrever na tela se o
# usuario perdeu ou venceu

num = randint(1,10)
print('The machine is thinking... ... ... ')
numUs = input('Tente descobrir o número : ')

if numUs == num:
    print('Parabéns, você venceu!')

else:
    print('A máquina ganhou, tente novamente!')

    print('O seu número foi {} e o da máquina foi {}'.format(numUs, num))