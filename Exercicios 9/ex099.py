from time import sleep


def maior(* nums):
    print('=-' * 30)
    print('Analisando os valores passados...')
    list_val = list(nums)

    if len(list_val) == 0:
        print('Foram informados 0 valores ao todo.')
        print('O maior valor informado foi 0')
    else:
        print(f'Foram informados {len(nums)} valores ao todo.')
        
        for i in list_val:
            print(i, end=' ', flush=True)
            sleep(0.5)

        print(f'O maior valor informado foi {max(nums)}')


maior(2,3,4)
maior(6,8)
maior(2,3,4,7,9,5,1)
maior()