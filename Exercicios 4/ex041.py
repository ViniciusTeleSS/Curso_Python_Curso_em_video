from datetime import datetime

nasci = int(input('Ano de nascimento: '))
data = datetime.now()
idade = data.year - nasci

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
