lt1 = []
lt2 = []
for i in range(10, 21):
    lt1.append(i)
    if i % 2 == 0:
        lt2.append(i)
print('vetor: {}'.format(lt1))
lt2.sort(reverse=True)
print('Os numeros pares são: {}'.format(lt2))
