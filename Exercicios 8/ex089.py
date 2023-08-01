
alunos = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media =  (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    cont = input('Quer continuar? [S/N] ')

    if cont in 'Nn':
        break

print('=-' * 20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)

for i, v in enumerate(alunos):
    print(f'{i:<4}{v[0]:<10}{v[2]:>8.1f}')

while True:

    notas = int(input('Mostrar notas de qual aluno? (999 interrompe) '))

    if notas == 999:
        print('FINALIZANDO...')
        break
    if notas <= len(alunos):
        print(f'Notas de {alunos[notas][0]} são {alunos[notas][1]}')
print('VOLTE SEMPRE')    


