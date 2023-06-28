while True:
    n = int(input('Deseja saber a tabuada de qual número: '))
    if n < 0:
        break
    for i in range(1, 11):
        result = n * i
        print(f'{n} X {i} = {result} ')
print('Programa finalizado')
