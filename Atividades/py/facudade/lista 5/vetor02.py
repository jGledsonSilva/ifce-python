lt1 = []
lt2 = []
for i in range(2, 21):
    if i % 2 == 0:
        lt1.append(i ** 2)
print('vetor 1:', lt1)

for i in range(10, 20):
    lt2.append(i)
print('vetor 2:', lt2)

slt = [''] * len(lt1)
for i in range(len(lt1)):
    slt = lt1 + lt2
    slt.sort()

print('A soma do vetor 1 e do vetor 2 é:', slt)
