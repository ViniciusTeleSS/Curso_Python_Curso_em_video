preço1 = float(input('Digite o preço do produto R$'))
valordesc = preço1 * 5 / 100
valorfinal = preço1 - valordesc

print(
    f'O preço do produto era R${preço1:.2f}, com 5% de desconto é de R${valorfinal:.2f}')
