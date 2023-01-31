nome = str(input('Digite o nome completo: '))
idade = int(input('Digite a idade: '))
tempo = int(18 - idade)
tempoa = int(idade - 18)
if idade < 18 :
    print('{} com {} anos, você ainda tem {} ano até o alistamento militar'.format(nome, idade, tempo, ))
elif idade == 18:
    print('{} com {} anos, já está na hora de se alistar!'
          'Aliste-se em https://alistamento.eb.mil.br'.format(nome, idade))
elif idade > 19:
    print('{} com {} anos, já passou da hora de se alistar, você passou {} anos da idade ideal para o alistamento! '
          'Consulte sua situação em : https://alistamento.eb.mil.br'.format(nome, idade, tempoa))