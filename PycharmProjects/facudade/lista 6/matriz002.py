matriz = [[], [], [], [], []]
m = 0
s = []
for l in range(0, 4):
    print('¨'*30)
    for c in range(0, 1):
        matriz[l].append(int(input('Digite o número da sua matricula:')))
    for c in range(1, 2):
        matriz[l].append(str(input('Digite o seu nome:')))
    for c in range(2, 3):
        matriz[l].append(str(input('Digite sua função:')))
    for c in range(3, 4):
        sal = (int(input('Digite o valor do salário:')))
        matriz[l].append(sal)
        s.append(sal)
        max_s = max(s)
        min_s = min(s)
print('¨' * 30)
for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[l][c]:^7}]', end='')
    print()
print(f'O maior salário é: {max_s}')
print(f'O menor salário é: {min_s}')
