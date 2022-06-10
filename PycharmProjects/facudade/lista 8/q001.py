print('Asequéncia da série Fibonacci até o 12º termo:')
a = 0
b = 0
c = 1
print(f'{b} {c}', end='')
for i in range(12):
    a = b
    b = c
    c = a + b
    print(f' {c}', end='')


