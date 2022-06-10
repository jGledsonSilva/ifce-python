matriz2 = [["times"], ["pg"], ["gm"], ["gs"], ["s"], ["v"], ["ga"], [], [], [], [], []]
for l in range(1, 3):
    for c in range(0, 1):
        matriz2[l].append(str(input(f'Digite o nome do time {l}:')))
    for c in range(1, 2):
        matriz2[l].append(0)
    for c in range(2, 3):
        matriz2[l].append(0)
    for c in range(3, 4):
        matriz2[l].append(0)
    for c in range(4, 5):
        matriz2[l].append(0)
    for c in range(5, 6):
        matriz2[l].append(0)
    for c in range(6, 7):
        matriz2[l].append(0)
print('-='*30)
p1 = (int(input(f'Digite o placar do time [{matriz2[1][0]}] : ')))
p2 = (int(input(f'Digite o placar do time [{matriz2[2][0]}] : ')))
if p1 > p2:
    matriz2[1][1] = 2
    matriz2[1][5] = 1
    matriz2[2][1] = 0
    matriz2[2][5] = 0
else:
    matriz2[2][1] = 2
    matriz2[2][5] = 1
    matriz2[1][1] = 0
    matriz2[1][5] = 0
if p1 == p2:
    matriz2[1][1] = 1
    matriz2[1][5] = 0
    matriz2[2][1] = 1
    matriz2[2][5] = 0
matriz2[1][2] = p1
matriz2[1][3] = p2
matriz2[1][4] = p1 - p2
matriz2[1][6] = p1 / p2
matriz2[2][2] = p2
matriz2[2][3] = p1
matriz2[2][4] = p2 - p1
matriz2[2][6] = p2 / p1
print('--'*30)
print(f'[{matriz2[1][0]}] x [{matriz2[2][0]}] / [{p1}] x [{p2}]')
print('--'*30)
for l in range(1, 3):
    for c in range(0, 7):
        print(f'[{matriz2[l][c]:^8}]',  end='')
    print()
w = 0
for l in range(1, 3):
    w = matriz2[l][1]
    matriz2[l][1] = matriz2[l][2]
    matriz2[l][2] = w

    ## Trocando Coluna de S por times
for l in range(1, 3):
    w = matriz2[l][3]
    matriz2[l][4] = matriz2[l][2]
    matriz2[l][2] = w

    ## ordenando lista
primeiaLinha = matriz2.pop(1)
matriz2.sort(reverse=True)
matriz2.insert(1, primeiaLinha)

# Desctrocando de S por Times
for l in range(1,3):
    w = matriz2[l][4]
    matriz2[l][4] = matriz2[l][2]
    matriz2[l][2] = w

# Destrocando do PG e TImes
for l in range(1, 3):
    w = matriz2[l][1]
    matriz2[l][1] = matriz2[l][2]
    matriz2[l][2] = w
print('[ times  ][   pg   ][   gm   ][   gs   ][   s    ][   v    ][   ga   ]')
for l in range(1, 3):
    for c in range(0, 7):
        print(f'[{matriz2[l][c]:^8}]',  end='')
    print()
