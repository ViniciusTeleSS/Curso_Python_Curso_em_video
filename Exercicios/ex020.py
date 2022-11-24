from random import shuffle

nome1 = str(input('Digite o nome de um aluno: '))
nome2 = str(input('Digite o nome de um aluno: '))
nome3 = str(input('Digite o nome de um aluno: '))
nome4 = str(input('Digite o nome de um aluno: '))
nomes = [nome1, nome2, nome3, nome4]
ordem = shuffle(nomes)


print(f'A ordem sorteada para a apresentação é:\n{nomes}')
