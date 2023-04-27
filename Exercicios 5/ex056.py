
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
totalmulher20 = 0

for i in range(1, 5):
    print(f'-----{i}º PESSOA-----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    somaidade += idade

    if i == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if idade > 20 and sexo in 'Ff':
        totalmulher20 += 1

mediaidade = somaidade / 4
print(f'A média de idades do grupo é de {mediaidade:.0f} anos')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomemaisvelho}')
print(f'E o total de mulheres com mais de 20 anos é de {totalmulher20}')
