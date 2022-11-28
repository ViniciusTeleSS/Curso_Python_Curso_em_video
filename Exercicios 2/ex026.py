frase = input('Digite uma frase: ').lower().strip()

counta = frase.count('a')

print(f'A letra "a" aparece {counta} vezes')
print('Aparece pela primeira vez na posição', frase.find('a')+1)
print('Aparece pela ultima vez na posição ', frase.rfind('a')+1)
