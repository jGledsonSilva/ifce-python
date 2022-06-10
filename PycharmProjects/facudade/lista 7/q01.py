n1 = int(input('Digite o número:'))
n2 = int(input('Digite o segundo número:'))
c = str(input('Digite o caractere para operação:'))

if c == '+':
    print(f'O resultado da soma: {n1} {c} {n2} = {n1+n2}')
elif c == '-':
    print(f'O resultado da subtração: {n1} {c} {n2} = {n1-n2}')
elif c == '/':
    print(f'O resultado da divisão: {n1} {c} {n2} = {n1/n2}')
elif c == '*':
    print(f'O resultado da multiplicação: {n1} {c} {n2} = {n1*n2}')
else:
    print('Operação inválida')
