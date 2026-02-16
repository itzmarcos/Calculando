from modulos import mods
from time import sleep
print('\033[36mINICIANDO O PROGRAMA...\033[m')
while True:
    sleep(1)
    op = mods.opcao(['SOMA', 'MULTIPLICAÇÇÃO', 'DIVISÃO', 'SUBTRAÇÃO', 'SAIR DO SISTEMA'])
    if op == 1:
        sleep(0.5)
        mods.texto('\033[31mSOMA\033[m')
        print(f'Resultado: {mods.somar()}')
    if op == 2:
        sleep(0.5)
        mods.texto('\033[32mMULTIPLICAÇÃO\033[m')
        print(f'Resultado: {mods.mult()}')
    if op == 3:
        sleep(0.5)
        mods.texto('\033[33mDIVISÃO\033[m')
        print(f'Resultado: {mods.dividir()}')
    if op == 4:
        sleep(0.5)
        mods.texto('\033[34mSUBTRAÇÃO\033[m')
        print(f'Resultado: {mods.diminuir()}')
    if op == 5:
        print('\033[35mPROGRAMA FINALIZADO...\033[m')
        break