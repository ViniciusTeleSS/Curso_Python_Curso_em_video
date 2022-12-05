from datetime import datetime

ano = int(input('Digite o seu ano de nascimento: '))
data = datetime.now()
idade = data.year - ano

print(idade)

if idade < 18:
    tempo = 18 - idade
    print(
        f'Você não precisa se alistar ainda, faltam {tempo} anos para precisar')
elif idade == 18:
    print('Você está no tempo para se alistar')
else:
    tempo = idade - 18
    print(f'Você precisa se alistar ja passou {tempo} ano do prazo')
