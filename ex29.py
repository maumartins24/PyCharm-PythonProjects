print('A VELOCIDADE DA VIA É 80KM/H')
vel = float(input('Qual a velocidade do carro? '))
mta = (vel-80) * 7
if vel > 80:
    print('Você foi multado!')
    print('O valor da multa foi {:.2f}'.format(mta))
else:
    print('Velocidade aceita!')