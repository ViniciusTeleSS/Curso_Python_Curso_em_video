cont = 'S'
somatoria = 0
Qtd_Termos = 0
maior = 0
menor = 0

while cont == 'S':
    num1 = int(input('Digite um número: '))
    somatoria += num1
    Qtd_Termos += 1
    cont = input('Deseja continuar? [S/N]: ').upper()
    if Qtd_Termos == 1:
        maior = menor = num1
    else:
        if num1 > maior:
            maior = num1
        if num1 < menor:
            menor = num1
print(
    f'Você digitou {Qtd_Termos} numeros e a média foi {somatoria/Qtd_Termos:.2f}')
print(f'O maior valor foi de {maior} e o menor foi de {menor}')
