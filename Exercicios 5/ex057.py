
sexos = ['M', 'F']
usuario_sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip()

while usuario_sexo not in sexos:
    usuario_sexo = input('Opção inválida, tente novamente: ').upper().strip()
print(f'Sexo {usuario_sexo} registrado com sucesso!')
