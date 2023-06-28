print("LOJA LOJA")

total = 0
maior_mil = 0
mais_barato = ""
menor_preco = 0
contador = 0

while True:
    prod = input("Nome do produto: ")
    preco = float(input("Preço R$"))
    total += preco
    contador += 1

    if preco > 1000:
        maior_mil += 1

    if contador == 1 or preco < menor_preco:
        menor_preco = preco
        mais_barato = prod

    cont = input("Quer continuar? [S/N]").upper()

    if cont == "N":
        break

print("FIM DO PROGRAMA")
print(
    f"""O total da compra foi de R${total}
Temos {maior_mil} produtos custando mais de R$1000.00
O produto mais barato foi {mais_barato} que custa R${menor_preco}"""
)
