matriz = [[], [], [], [], []]
for l in range(1, 5):
    for c in range(1, 4):
        matriz[l].append(0)
print('¨' * 30)
for l in range(1, 5):
    for c in range(1, 4):
        print(f'[{matriz[l][c]:^7}]', end='')
    print()
