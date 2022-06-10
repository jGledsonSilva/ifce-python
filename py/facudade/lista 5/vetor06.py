lt = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(input('Digite um numero:'))
if num not in lt:
    print('Esse nummero não estar no vetor!')
else:
    i = lt.index(num)
print('O nunmero {} esta na posição {} do vetor: {} '.format(num, i, lt))
