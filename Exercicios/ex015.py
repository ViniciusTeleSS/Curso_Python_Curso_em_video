dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
preço_dia = 60 * dias
preço_km = 0.15 * km
preço_total = preço_dia + preço_km

print(
    f'O total a ser pago por {dias} dias alugados, no valor de R$60.00 por dia, com uma taxa de R$0.15 por km é de {preço_total:.2f}')
