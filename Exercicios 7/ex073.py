times_2018 = ('Palmeiras','Flamengo','Internacional','Grêmio','São Paulo','Atlético-MG','Athletico-PR','Cruzeiro',
              'Botafogo','Santos','Bahia','Fluminense','Corinthians','Chapecoense','Ceará','Vasco','Sport','América-MG','Vitória','Paraná')

print(f'Os 5 primeiros colocados são {times_2018[:5]}')
print(f'Os 4 último colocados são {times_2018[-4:]}')
print(f'Times em ordem alfabética {sorted(times_2018)}')
print(f'O chapecoense está em {times_2018.index("Chapecoense")+1}º posição')
