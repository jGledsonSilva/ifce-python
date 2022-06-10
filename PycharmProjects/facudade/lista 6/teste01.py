import math
import random
from time import time

times = []
partidas = []
quantidadeDeTimes = int(input('Digite a quantidade Total de times: '))
tabela = [['TIMES', 'PG', 'GM', 'GS', 'S', 'V', 'GA']]


def achandoValorNoarrayEAdicionandoMaisUM(array, time, valor, atributo):
    posisitonOfAtributte = 0

    for qualE in array[0]:
        for position in range(0, len(array[0])):
            if atributo == array[0][position]:
                posisitonOfAtributte = position

    for l in array:
        if l[0] == time:
            l[posisitonOfAtributte] = l[posisitonOfAtributte] + valor
    return array


# Inverter os valores da lista
def inverterLista(lista):
    listInvertida = []
    idx = len(lista) - 1
    while (idx >= 0):
        listInvertida.append(lista[idx])
        idx = idx - 1

    return listInvertida


## criando uma sublista
def dadoDoTime(nome, pg, gm, cs, s, v, ga):
    dadosDostimes = [nome, pg, gm, cs, s, v, ga]
    return dadosDostimes


## printando a tabela no terminal
def tabelaDeJogos():
    linhas = len(tabela)
    colunas = len(tabela[0])
    for l in range(0, linhas):
        for c in range(0, colunas):
            print(f'[{tabela[l][c]:^13}]', end='')
        print()


## Para saber a quantidade total de jogos iremos fazer uma combinação com o total de times
## agrupando de 2 em 2
## formula de combinação: N!/P!(N-P)!
quantidadeDeJogos = int(
    (math.factorial(quantidadeDeTimes)) / (math.factorial(2) * math.factorial(quantidadeDeTimes - 2)))

lista = 0
## aqui estou adicionando os nomes dos times de acorda com a quantidade
for n in range(0, quantidadeDeTimes):
    times.append(input(f'Digite o nome do {n + 1}° time: '))

for n in times:
    lista = dadoDoTime(n, 0, 0, 0, 0, 0, 0)
    tabela.append(lista)


## verificando se a sublista já existe dentro da lista
def verificarSeExistJogos(jogos):
    timeInvertido = inverterLista(jogos)
    # print(timeInvertido)
    if jogos in partidas:
        return True
    elif timeInvertido in partidas:
        return True
    return False


# Identificando qual time ganhou
def qualTimeGanhou(time):
    if time[2] > time[3]:
        achandoValorNoarrayEAdicionandoMaisUM(tabela, time[0], 2, 'PG')
        achandoValorNoarrayEAdicionandoMaisUM(tabela, time[0], 1, 'V')

    elif time[2] == time[3]:
        achandoValorNoarrayEAdicionandoMaisUM(tabela, time[0], 1, 'PG')
        achandoValorNoarrayEAdicionandoMaisUM(tabela, time[1], 1, 'PG')

    elif time[2] < time[3]:
        achandoValorNoarrayEAdicionandoMaisUM(tabela, time[1], 2, 'PG')
        achandoValorNoarrayEAdicionandoMaisUM(tabela, time[1], 1, 'V')


# estou declarando todos os possivei  jogos
while len(partidas) < quantidadeDeJogos:
    time1 = times[random.randint(0, quantidadeDeTimes - 1)]
    time2 = times[random.randint(0, quantidadeDeTimes - 1)]

    if time1 == time2:
        continue

    jogos = [time1, time2]
    if verificarSeExistJogos(jogos):
        continue
    partidas.append(jogos)

for partida in partidas:
    yesOrNot = input(f'A partida {partida[0]} x {partida[1]} já ocorreu? [S/N]')
    if yesOrNot == 'S' or yesOrNot == 's' or yesOrNot == 'sim':
        # colocar o placa dentro da lista
        golsDoPrimeiroTime = int(input(f'Dgitite a quantidade de gols dessa partida do time {partida[0]} : '))
        golsDoSegundoTime = int(input(f'Dgitite a quantidade de gols dessa partida do time {partida[1]} : '))

        partida.append(golsDoPrimeiroTime)
        partida.append(golsDoSegundoTime)
        # Colocando a quantidade de gols marcados
        achandoValorNoarrayEAdicionandoMaisUM(tabela, partida[0], golsDoPrimeiroTime, 'GM')
        achandoValorNoarrayEAdicionandoMaisUM(tabela, partida[1], golsDoSegundoTime, 'GM')

        # Colocando a quantidade de gols sofrindos
        achandoValorNoarrayEAdicionandoMaisUM(tabela, partida[0], golsDoSegundoTime, 'GS')
        achandoValorNoarrayEAdicionandoMaisUM(tabela, partida[1], golsDoPrimeiroTime, 'GS')

        # Colocando o número de pontos ganhos
        qualTimeGanhou(partida)

        # Calculando o saldo de gols do Primeiro Time
        saldosDeGolsPrimeiroTime = golsDoPrimeiroTime - golsDoSegundoTime
        achandoValorNoarrayEAdicionandoMaisUM(tabela, partida[1], saldosDeGolsPrimeiroTime, 'S')

        # Calculando o saldo de gols do Segundo Time
        saldosDeGolsPrimeiroTime = golsDoSegundoTime - golsDoPrimeiroTime
        achandoValorNoarrayEAdicionandoMaisUM(tabela, partida[2], saldosDeGolsPrimeiroTime, 'S')


def adicionandoGA():
    for l in range(1, len(tabela)):
        GS = tabela[l][3]
        GM = tabela[l][2]
        time = tabela[l][0]
        if GS == 0:
            GS = 1
        GA = GM / GS
        GA_formatado = "{:.2f}".format(GA)
        achandoValorNoarrayEAdicionandoMaisUM(tabela, time, float(GA_formatado), 'GA')


adicionandoGA()
print()
print('ITEM A ')
print()
tabelaDeJogos()
print()
print('=' * 100)
print('item B')
print()


###########################################################################################################################################################################
# QUESTÃO B
# QUANTO O SORT É USADO PARA UMA SUBLISTA ELE ORDENA PELA PRIEMIRA ARRAY DENTRO DA SUBTLISTA, E SE FOR IGUAL ELE VAI PARA O SEGUNDO ARRAY DA SUBLISTA E ASSIM POR DIANTE
# ESTOU COLOCANDO EM ORDEM DE PESOS, A COLUNA COM MAIS PESO VAI PARA O PRIEMRIO, A SEGUNDO COM MAIS PESO  PARA SEGUNDA ARRAY E ASSIM POR DIANTE
# E DEPOIS EU FAÇOR UM SORT REVERSE
# DEPOIS DESTROCO AS COLUNAS E MOSTRO NA TELA A TABELA ORDENADA

def ordenandoListDeAcordoComPG(tabela):
    linhas = len(tabela)
    ## Trocando de coluna do PF e TIMES para orderna a lista
    for l in range(0, linhas):
        variaAux = tabela[l][0]
        tabela[l][0] = tabela[l][1]
        tabela[l][1] = variaAux

    ## Trocando Coluna de S por times
    for l in range(0, linhas):
        variaAux = tabela[l][3]
        tabela[l][3] = tabela[l][1]
        tabela[l][1] = variaAux

    ## ordenando lista
    primeiaLinha = tabela.pop(0)
    tabela.sort(reverse=True)
    tabela.insert(0, primeiaLinha)

    # Desctrocando de S por Times
    for l in range(0, linhas):
        variaAux = tabela[l][3]
        tabela[l][3] = tabela[l][1]
        tabela[l][1] = variaAux

    # Destrocando do PG e TImes
    for l in range(0, linhas):
        variaAux = tabela[l][0]
        tabela[l][0] = tabela[l][1]
        tabela[l][1] = variaAux


ordenandoListDeAcordoComPG(tabela)
tabelaDeJogos()