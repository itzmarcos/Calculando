from modulos import mods
from time import sleep
while True:
    sleep(1)
    op = mods.opcao(['SOMA', 'MULTIPLICAÇÇÃO', 'DIVISÃO', 'SUBTRAÇÃO', 'SAIR DO SISTEMA'])
    if op == 1:
        sleep(0.5)
        mods.texto('SOMA')
        print(f'O resultado da some foi {mods.somar()}')
    if op == 2:
        sleep(0.5)
        mods.texto('MULTIPLICAÇÃO')
        print(f'O resultado da multiplicação foi {mods.mult()}')
    if op == 3:
        sleep(0.5)
        mods.texto('DIVISÃO')
        print(f'O resultado da divisão foi {mods.dividir()}')
    if op == 4:
        sleep(0.5)
        mods.texto('SUBTRAÇÃO')
        print(f'O resultado da some foi {mods.diminuir()}')
    if op == 5:
        print('Programa FINALIZADO')
        break