num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
print(num1, "&", num2)

if num1 > num2:
    print('O \033[;35m primeiro valor \033[m é \033[;34m maior \033[m')
elif num2 > num1 :
    print('O \033[;35m segundo valor \033[m é \033[;34m maior \033[m')
else:
    print('\033[;35m Não existe \033[m valor maior, os dois são \033[;34m iguais \033[m')
