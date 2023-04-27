n = 0
somatoria = 0
Qtd_Termos = 0

n = int(input('Digite um numero [999 para finalizar o programa]: '))

while n != 999:
    somatoria += n
    Qtd_Termos += 1
    n = int(input('Digite um numero [999 para finalizar o programa]: '))
print(f'A quantidade total de termos digitados foi de {Qtd_Termos}')
print(f'E a soma de todos os termos digitados é de {somatoria}')
