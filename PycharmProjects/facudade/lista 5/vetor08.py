lt = []
lt1 = []
lt2 = set()

for i in range(10):
    n = int(input('Digite um numero:'))
    lt.append(n)

for j in lt:
    if j not in lt1:
        lt1.append(j)
    else:
        lt2.add(j)
a = len(lt2)
print('Vetor: {}'.format(lt))
print('Vetor sem repetição: {}'.format(lt1))
print('São {} numero(s) que se repete.'.format(a))
print('Vetores repetidos: {}'.format(lt2))
