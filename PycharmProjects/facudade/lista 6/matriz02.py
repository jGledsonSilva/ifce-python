M = [[]]

for i in range(1, 5):
    print('¨'*60)
    print(f'{i}º funcionário.')
    sa = []
    linha = [int(input('Digite o número da sua matricula:')),
             str(input('Digite o seu nome:')),
             str(input('Digite sua função:'))]
    s = (int(input('Digite o seu salário:')))
    linha.append(s)
    sa.append(s)
    M.append(linha)
    max_sa = max(sa)
    min_sa = min(sa)
print('='*30)
for i in range(1, 5):
    print(M[i])
print(f'O maior salário é: {max_sa}')
print(f'O menor salário é: {min_sa}')
