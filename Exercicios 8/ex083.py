ex = str(input('Digite a expressão: '))
pilha = []

for i in ex:
    if i == '(':
        pilha.append('(')
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada')
