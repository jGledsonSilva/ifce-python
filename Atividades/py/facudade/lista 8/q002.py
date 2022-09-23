cédula: list[int] = [2, 5, 10, 20, 50, 100, 200]
v = int(input('Digite o valor do saque:'))
t = v
c = cédula[6]
tc = 0
s = 0
while True:
    if t >= c:
        t -= c
        tc += 1
    else:
        if tc > 0:
            s += tc
            print(f'Total de {tc} cédula de R${c}')
        if c == cédula[6]:
            c = cédula[5]
        elif c == cédula[5]:
            c = cédula[4]
        elif c == cédula[4]:
            c = cédula[3]
        elif c == cédula[3]:
            c = cédula[2]
        elif c == cédula[2]:
            c = cédula[1]
        elif c == cédula[1]:
            c = cédula[0]
        tc = 0
        if t == 0:
            break
print('='*27)
print(f'No total de {s} cédula.')

