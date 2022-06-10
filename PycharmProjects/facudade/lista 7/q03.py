n1 = float(input('Digite um número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro: '))
if n1 > n3:
    n1, n3 = n3, n1
if n1 > n2:
    n1, n2 = n2, n1
if n2 > n3:
    n2, n3 = n3, n2
print(f'A forma crescente: {n1}; {n2}; {n3}')
