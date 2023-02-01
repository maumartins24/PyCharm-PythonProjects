peso = float(input('Digite seu peso : Kg.'))
altura = float(input('Digite sua altura: M'))
imc = (peso / (altura * altura))
print('Com Kg{} e {} de altura seu imc é de {:.2f}'.format(peso, altura, imc))
if imc < 18.5:
    print('Diante o Índice de Massa Corpórea você está abaixo do peso! ')
elif  imc == 18 or imc <= 25:
    print('Diante o Índice de Massa Corpórea você está no peso ideal!')
elif imc == 25.01 or imc <=30:
    print('Diante o Índice de Massa Corpórea você está no sobrepeso!')
elif imc == 30.01 or imc <= 40:
    print('Diante o Índice de Massa Corpórea você está na obesidade!')
else:
    print('Diante o Índice de Massa Corpórea você está com obesidade mórbida!')