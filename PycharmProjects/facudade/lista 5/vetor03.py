lt1 = []
lt2 = []
for c in range(10):
    n = int(input('Digite um número:'))
    d = 0
    lt1.append(n)
    for di in range(1, n):
        if n % di == 0:
            d += 1
    if d > 1:
        var = None
    else:
        lt2 += [n]
print('Vetor: {}'.format(lt1))
print('Os primos nesse vetor são {}'.format(lt2))
