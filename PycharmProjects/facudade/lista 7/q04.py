dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))
v = False
if mes == 1:
    mes = 'Janeiro'
    if dia <= 31:
        v = True
elif mes == 2:
    mes = 'Fevereiro'
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        if dia <= 29:
            v = True
    elif dia <= 28:
        v = True
elif mes == 3:
    mes = 'Março'
    if dia <= 31:
        v = True
elif mes == 4:
    mes = 'Abril'
    if dia <= 30:
        v = True
elif mes == 5:
    mes = 'Maio'
    if dia <= 31:
        v = True
elif mes == 6:
    mes = 'junho'
    if dia <= 30:
        v = True
elif mes == 7:
    mes = 'Julho'
    if dia <= 31:
        v = True
elif mes == 8:
    mes = 'Agosto'
    if dia <= 31:
        v = True
elif mes == 9:
    mes = 'Setembro'
    if dia <= 30:
        v = True
elif mes == 10:
    mes = 'Outubro'
    if dia <= 31:
        v = True
elif mes == 11:
    mes = 'Novembro'
    if dia <= 30:
        v = True
elif mes == 12:
    mes = 'Dezembro'
    if dia <= 31:
        v = True
if v:
    print(f'Data válida, {dia} de {mes} de {ano}')
else:
    print('Data inválida.')
