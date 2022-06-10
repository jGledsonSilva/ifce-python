matriz = [[], [], [], [], []]
me = men = 0
for l in range(1, 3):
    for c in range(0, 1):
        matriz[l].append(str(input(f"Digite o nome do corredor {l}: ")))
    for c in range(1, 11):
        matriz[l].append(float(input(f"Digite o tempo da volta {c} em segundos: ")))
print('¨' * 30)
for l in range(1, 3):
    for c in range(0, 11):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
for c in range(1, 11):
    if c == 1:
        me = matriz[1][c]
    elif matriz[1][c] < me:
        me = matriz[1][c]
for c in range(1, 11):
    if c == 1:
        men = matriz[2][c]
    elif matriz[2][c] < men:
        men = matriz[2][c]
print(me)
print(men)
