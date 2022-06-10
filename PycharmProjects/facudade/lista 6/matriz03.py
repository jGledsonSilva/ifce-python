matriz = [[], [], [], [], []]
slin = slin1 = slin2 = 0
scol = scol1 = scol2 = 0
sdi = sdi1 = 0
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
for l in range(0, 3):
    scol += matriz[l][0]
    scol1 += matriz[l][1]
    scol2 += matriz[l][2]

for l in range(0, 3):
    sdi += matriz[l][l]

for l in range(0, 3):
    sdi1 += matriz[l][l]
print(f'{sdi1}')
if slin == slin1 == slin2 == scol == scol1 == scol2 == sdi == sdi1:
    print('É uma matriz Quadrado Mágico.')
else:
    print('Não é uma matriz Quadrado Mágico.')
