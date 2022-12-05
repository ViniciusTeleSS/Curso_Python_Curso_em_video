preco = float(input('Digite o valor total da compra: '))

condicao = int(input(
    'Escolha o numero da forma de pagamento: \n1-À vista dinheiro \n2-À vista no cartão \n3-Duas vezes no cartão \n4-Três vezes ou mais no cartão \n'))

if condicao == 1:
    preco_novo = preco - (preco * 10 / 100)
    print(
        f'O preço final da compra com 10% de desconto será de R${preco_novo} ')
elif condicao == 2:
    preco_novo = preco - (preco * 5 / 100)
    print(
        f'O preço final da compra com 5% de desconto será de R${preco_novo} ')
elif condicao == 3:
    print('O valor da compra continua o mesmo')
elif condicao == 4:
    preco_novo = preco + (preco * 20 / 100)
    print(
        f'O preço final da compra com 20% de juros será de R${preco_novo} ')
else:
    print('Opção inválida')
