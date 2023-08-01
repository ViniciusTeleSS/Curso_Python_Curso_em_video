
aluno = {}

aluno['nome'] = str(input('Nome: ' ))
aluno['média'] = float(input(f'Média de {aluno["nome"]} '))

if aluno['média'] >= 7:
    aluno['situação'] = 'aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'

print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["média"]}')
print(f'Situação é igual a {aluno["situação"]}')