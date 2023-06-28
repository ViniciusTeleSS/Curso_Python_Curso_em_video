from random import randint

# MENU
carac = '-='*20
print(carac)
print('VAMOS JOGAR PAR OU IMPAR')
print(carac)

vencidas = 0

while True:

    # 1º FASE - ESCOLHA DO JOGADOR
    num_player = int(input('Digite um valor: '))
    choice_player = input('Par ou ímpar? [P/I]')

    # 2º FASE - ESCOLHA DO PC
    num_pc = randint(0, 10)

    # 3º FASE - CONFERÊNCIA DO RESULTADO
    total = num_player + num_pc

    if total % 2 == 0:
        result = 'PAR'
    else:
        result = 'ÍMPAR'
    print(
        f'Você jogou {num_player} e o computador {num_pc}. Total de {total} DEU {result}')

    # 4º FASE - EXIBINDO O VENCEDOR
    if choice_player in 'Pp' and result == 'PAR':
        print('VOCÊ VENCEU')
        vencidas += 1
        print('REVANCHE')
    elif choice_player in 'Ii' and result == 'ÍMPAR':
        print('VOCÊ VENCEU')
        vencidas += 1
        print('REVANCHE')
    else:
        print('VOCÊ PERDEU')
        break
if vencidas > 1:
    print(f'Você ganhou {vencidas} rodadas')
elif vencidas == 1:
    print(f'Você ganhou {vencidas} rodada')
else:
    print(f'Você ganhou {vencidas} rodadas')
