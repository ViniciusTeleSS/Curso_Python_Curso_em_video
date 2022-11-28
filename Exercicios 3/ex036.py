from time import sleep

char1 = '-=-'
charqtd = 20
printchar = char1 * charqtd


# CABEÇALHO DO PROGRAMA
print(printchar)
print('BEM VINDO AO SIMULADOR DE FINANCIAMENTO DE CASAS')
print(printchar)

# COLETANDO INFORMAÇÕES
print('Primeiramente, vamos precisar de algumas informações:\n')
valor = float(input('1º: Qual é o valor da casa que deseja financiar? R$'))
salario = float(input('2º: Qual é o seu sálario? R$'))
anos = int(input('3º: Em quantos anos você deseja parcelar este valor? '))

print(printchar)
print('PROCESSANDO...')
sleep(2)
print(printchar)

# RESULTADO
anos_p_mes = anos * 12
valor_parcela = valor / anos_p_mes

if valor_parcela > salario * 30 / 100:
    print(
        f'Empréstimo NEGADO\nO valor da parcela é de R${valor_parcela:.2f} e excede 30% de seu sálario.')
else:
    print(
        f'Empréstimo APROVADO\nO valor da parcela ficou em R${valor_parcela:.2f}\nSeu empréstimo está dentro das regras, poderá solicitar se desejar.')
