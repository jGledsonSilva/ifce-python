corrida = {}
cont = 0
while cont < 2:
  nome = input(f"Digite o nome do corredor {cont+1}: ")
  voltas = []
  cont_v = 0
  while cont_v < 2:
    tempo = float(input(f"Digite o tempo da volta {cont_v+1} em segundos: "))
    voltas.append(tempo)
    cont_v += 1
  corrida[nome] = voltas
  cont += 1
melhor_volta = []
for nome in corrida:
  voltas = corrida[nome]
  melhor = voltas[0]
  for volta in voltas:
    if melhor > volta:
      melhor = volta
  melhor_volta.append([nome, melhor])
print(melhor_volta)


