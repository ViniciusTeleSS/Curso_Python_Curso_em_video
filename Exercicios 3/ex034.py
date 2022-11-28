salario = float(input('Digite o seu salário: '))

if salario > 1250:
    novo_salario = (salario * 10 / 100) + salario
    print(
        f'O seu salário receberá um aumento de 10% e passará a ser de {novo_salario}')
else:
    novo_salario = (salario * 15 / 100) + salario
    print(
        f'O seu salário receberá um aumento de 15% e passará a ser de {novo_salario}')
