from random import choice

nome1 = input('Digite o nome de um aluno: ')
nome2 = input('Digite o nome de um aluno: ')
nome3 = input('Digite o nome de um aluno: ')
nome4 = input('Digite o nome de um aluno: ')
aluno = [nome1, nome2, nome3]
choseone = choice(aluno)

print(f'O aluno escolhido para apagar o quadro foi {choseone}')
