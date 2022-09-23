lt = []
lt1 = []
lt2 = []
for i in range(10):
    n = int(input('Digite um número:'))
    lt.append(n)
    if n % 2 == 0:
        lt1.append(n)
    else:
        lt2.append(n)
q = len(lt1)
s = len(lt2)
print('vetor: {}'.format(lt))
print('São {} numeros pares que são: {}'.format(q, lt1))
print('São {} numeros ímpares que são: {}'.format(s, lt2))
