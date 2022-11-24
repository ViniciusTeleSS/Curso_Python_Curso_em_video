aumento = float(input('Digite a porcentagem do aumento '))
salario = float(input(
    f'Dgite seu salário para saber quanto ganhará com {aumento:.2f}% de aumento R$'))
valoraumento = salario * aumento / 100
salariofinal = salario + valoraumento

print(
    f'Após o aumento de {aumento:.2f}%, o seu salário de R${salario} passará a ser de R${salariofinal:.2f}')
print(f'Foi aumentado em seu salário R${valoraumento:.2f}')
