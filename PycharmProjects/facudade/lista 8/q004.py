matriz = [[], [], [], [], []]
slin = slin1 = slin2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]:')))
print('¨' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
for c in range(0, 3):
    slin += matriz[0][c]
    slin1 += matriz[1][c]
    slin2 += matriz[2][c]
if slin > slin1 and slin > slin2:
        print(f'A linha com maior soma é: [{matriz[0][0]}][{matriz[0][1]}][{matriz[0][2]}] = [{slin}]')
elif slin1 > slin and slin1 > slin2:
        print(f'A linha com maior soma é: [{matriz[1][0]}][{matriz[1][1]}][{matriz[1][2]}] = [{slin1}]')
elif slin2 > slin and slin2 > slin1:
        print(f'A linha com maior soma é: [{matriz[2][0]}][{matriz[2][1]}][{matriz[2][2]}] = [{slin2}]')
