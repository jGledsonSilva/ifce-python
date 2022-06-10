def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)


n = int(input('Digite o maior número:'))
v = int(input('Digite o menor número:'))
a = n
b = v

print(f'O mdc({a}, {b}) = {mdc(a, b)}')

