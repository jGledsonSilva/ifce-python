m = [[]]
for i in range(1, 3):
    print('#'*60)
    print(f'Cliente {i}')
    linha = [int(input('Digite o número da conta:')),
             str(input('Digite o seu nome:'))]
    saldo = (int(input('informe o seu saldo:')))
    debi = (int(input('Qual o valor do seu saque:')))
    linha.append(saldo)
    linha.append(debi)
    if debi > saldo:
        print('Saldo insuficiente')
    else:
        st = saldo - debi
        print(f'Seu saldo atual é de: {st}')
    linha.append(st)
    m.append(linha)
print('#='*30)
for i in range(1, 3):
    print(m[i])
