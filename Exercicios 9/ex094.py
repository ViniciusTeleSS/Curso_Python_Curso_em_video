import math

galera = []
pessoa = {}
soma = media = 0

while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor digite apenas S ou N.')
    if resp == 'N':
        break

print(f'Foram cadastradas {len(galera)} pessoas')
print(f'A media de idade é de {soma / len(galera)} anos')
print('As mulheres cadastradas foram: ' ,end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]},',end='')
print()
print('As pessoas com idade acima da média são: ', end='')
for p in galera:
    if p['idade'] >= soma / len(galera):
        print(f'{p["nome"]}')
print()

