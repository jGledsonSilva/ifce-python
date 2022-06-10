p = float(input('Digite o peso: '))
a = float(input('Digite a altura: '))

imc = p / (a*a)

if imc < 18.5:
    c = 'Magreza'
    o = 0
elif 18.5 <= imc <= 24.9:
    c = 'Normal'
    o = 0
elif 25 <= imc <= 29.9:
    c = 'Sobrepeso'
    o = 1
elif 30 <= imc <= 39.9:
    c = 'Obesidade'
    o = 2
elif imc >= 40:
    c = 'Obesidade grave'
    o = 3
print(f'imc: {imc}')
print(f'Classificação: {c}')
print(f'Grau de obesidade: {o}')
