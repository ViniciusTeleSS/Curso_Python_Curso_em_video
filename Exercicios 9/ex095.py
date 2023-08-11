jogador = {}
partidas = []
galera = []

while True:
    partidas.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for c in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partida {c} ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    galera.append(jogador.copy())

    resp = str(input('Deseja continuar? [S/N] ')).upper()[0]

    if resp == 'N':
        break

print('=-' * 30)
print(galera)

print('=-' * 20)
print(f'{"No.":<4}{"NOME":<10}{"GOLS":>8}{"TOTAL":>8}')
print('-' * 30)

for i, v in enumerate(galera):
    print(f'{i:<4}{galera[i]["nome"]}{galera[i]["gols"]}{galera[i]["total"]}')
print('-' * 30)

while True:

    dados = int(input('Mostrar dados de qual jogador? (999 interrompe) '))

    if dados == 999:
        print('FINALIZANDO...')
        break
    if dados >= len(galera):
        print(f'ERRO! Não existe jogador com o código {dados}! Tente novamente')
    if dados < len(galera):
        print(f'Levantamento do jogador {galera[dados]["nome"]}')
        for i, v in enumerate(jogador['gols']):
            print(f'Na partida {i} fez {v} gols.')
print('VOLTE SEMPRE')    




