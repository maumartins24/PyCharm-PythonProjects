print('___ CONFEDERAÇÃO NACIONAL DE NATAÇÃO ___')

ano = int(input('Digite o ano de nascimento do atleta: '))
idade = (2023 - ano)
if idade <= 9:
    print('Com {} anos a categoria do atleta será MIRIM!'.format(idade))
elif idade <=14:
    print('Com {} anos a categoria do atleta será INFANTIL!'.format(idade))
elif idade <= 19:
    print('Com {} anos a categoria do atleta será JÚNIOR'.format(idade))
elif idade <= 25:
    print('Com {} anos a categoria do atleta será SÊNIOR'.format(idade))
else:
    print('Com {} anos a categoria do atleta será MASTER'.format(idade))
