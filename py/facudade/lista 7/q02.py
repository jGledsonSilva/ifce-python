m = float(input('Digite a media: '))
if 0 <= m <= 4.9:
    print('Conceito: D')
elif 5.0 <= m <= 6.9:
    print('Conceito: C')
elif 7.0 <= m <= 8.9:
    print('Conceito: B')
elif 9.0 <= m <= 10:
    print('Conceito: A')
else:
    print('Media inválida')
