valor = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o slário do comprador: R$ '))
anos = int(input('Digite em quantos anos pretende se pagar: '))
prestacao = (valor / (anos * 12))
minimo = salario * 30 / 10
print('O valor da casa é de {:.2f} e sera paga em {} anos,'
      ' e a prestação sera de {:.2f}'.format(valor, anos, prestacao ))
if prestacao < minimo:
    print('O financiamento foi negado!')
else:
    print('O financiamento foi aprovado!')