from time import sleep
nota1= float(input('Digite a primeira nota: '))
nota2= float(input('Digite a próxima nota: '))
media = float((nota1 + nota2) /2)
print('Mediante suas notas {} e {} a sua média foi: {} '.format(nota1, nota2, media))
print('E sua situação é ...')
sleep(3)
if media < 5.0:
    print('\033[;31m REPROVADO\033[m')
elif media == 5.0 or media < 6.9:
    print('\033[;33m RECUPERAÇÃO\033[m')
elif media >= 7.0:
    print('\033[;34m APROVADO, PARABÉNS!\033[m')