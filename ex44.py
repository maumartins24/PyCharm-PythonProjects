print('-='*20)
print('           ____ CAIXA ____')
print('-='*20)

preço = float(input('Digite o preço do produto: (R$) '))
print('''Formas de pagamento : 
[1]   À Vista dinheiro/cheque
[2]   À Vista no cartão
[3]   Em até 2x no cartão
[4]   3x ou mais no cartao''')

pagamento = int(input('Digite a forma de pagamento:'))

if pagamento == 1:
    desconto = preço - (preço * 10 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço,desconto))
elif pagamento == 2:
    desconto = preço - (preço * 5 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço,desconto))
elif pagamento == 3:
    parcela = preço / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço,preço))
else:
    juros = preço + (preço * 20 /100)
    parcela = int(input('Quantas parcelas? '))
    totalparc = juros / parcela
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(parcela, totalparc))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço,juros))