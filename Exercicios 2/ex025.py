nome = input('Digite seu nome completo: ').lower()

findsilva = 'silva' in nome

print(findsilva)

if findsilva == True:
    print('Seu nome contém Silva')
else:
    print('Seu nome não contém Silva')
