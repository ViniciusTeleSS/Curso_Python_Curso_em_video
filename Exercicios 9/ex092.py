from datetime import date

data_atual = date.today()
ano_atual = data_atual.year

trabalhor = {}

trabalhor['nome'] = str(input('Nome: ' ))
ano_nasc = int(input('Ano de nascimento: '))
trabalhor['idade'] = ano_atual - ano_nasc
trabalhor['CTPS'] = str(input('Carteira de trabalho (0 não tem): ' ))

if trabalhor['CTPS'] == '0':
    trabalhor['CTPS'] = '0'
else:
    trabalhor['contratação'] = int(input('Ano de contratação: ' ))
    trabalhor['salário'] = float(input('Salário: R$ '))
    trabalhor['aposentadoria'] = (trabalhor['contratação'] - ano_nasc ) + 35

print('=-' *30)
for k, v in trabalhor.items():
    print(f'{k} tem o valor {v}')