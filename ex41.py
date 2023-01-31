print('___ CONFEDERAÇÃO NACIONAL DE NATAÇÃO ___')

ano = int(input('Digite o ano de nascimento do atleta: '))
idade = (2023 - ano)
if idade <= 9:
    print('Com {} anos a categoria do atleta será MIRIM!'.format(idade))
elif idade <=14:
    print('Com {} anos a categoria do atleta será INFANTIL!'.format(idade))
else:
    print('com {} anos o atleta não se enquadra!'.format(idade))