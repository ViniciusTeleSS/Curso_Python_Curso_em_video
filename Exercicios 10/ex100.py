from random import randint

lista = []

def sorteia():
    print('Sorteando 5 valores da lista: ',end='')
    for i in range(0,5):
        lista.append(randint(0,10))
    print(lista,'PRONTO!')

def somaPar():
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {lista}, temos {soma}')        

sorteia()
somaPar()
