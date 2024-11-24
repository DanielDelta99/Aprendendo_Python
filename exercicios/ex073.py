times = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'São Paulo', 'Bahia', 'Cruzeiro', 'Internacional', 'Atlético-MG', 'Vasco', 'RB Bragantino', 'Juventude', 'Criciúma', 'Athletico-PR', 'Grêmio', 'Santos', 'Fluminense', 'Goiás', 'Corinthians', 'Atlético-GO')
print('Brasileirão')
print('------------')
for c in (times):
    print(c)
print('------------')
print('5 primeiros colocados')
for c in (times[0:5]):
    print(c)
print('------------')
print('4 ultimos colocados')
for c in (times[-5:-1]):
    print(c)
print('------------')
print('Em ordem alfabetica')
alpha = sorted(times)
for c in (alpha):
    print(c)
print('------------')
n = times.index('Goiás')
print(f'{times[n]} está na {n+1}° posição.')
