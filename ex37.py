import math
num = int(input('Digite um número: '))
print('1 para binário, 2 para octal e 3 para hexadecimal')
conversao = int(input('Selecione uma base de conversão: '))
if conversao == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)))
elif conversao == 2:
 print('{} convertido para octal é igual a {}'.format(num, oct(num)))
elif conversao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)))
