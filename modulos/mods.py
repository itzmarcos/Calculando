def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except:
            print('ERROR')
        else:
            return valor
        

def lin(t=42):
    return '-' * t


def texto(msg=0):
    print(lin())
    print(msg.center(42))
    print(lin())


def opcao(lista):
    texto('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} {item}')
        c += 1
    print(lin())
    opc = leiaInt('Opção: ')
    return opc


def somar(n1=0, n2=0, n3=0):
    while True:
        try:
            n1 = int(input('Numerador: '))
            n2 = int(input('Denominador: '))
            n3 = n1 + n2
        except:
            print('ERROR: Try Again')
        else:
            return n3
        

def mult(n1=0, n2=0, n3=0):
    while True:
        try:
            n1 = int(input('Numeador: '))
            n2 = int(input('Denominador: '))
            n3 = n1 * n2
        except:
            print('ERROR: Try Again')
        else:
            return n3
        
def dividir(n1=0, n2=0, n3=0):
    while True:
        try:
            n1 = int(input('Numerador: '))
            n2 = int(input('Demoninador: '))
            n3 = n1 / n2
        except:
            print('ERROR, try again')
        else:
            return f'{n3:.0f}'
def diminuir(n1=0, n2=0, n3=0):
    while True:
        try:
            n1 = int(input('Numerador: '))
            n2 = int(input('Denominador: '))
            n3 = n1 - n2
        except:
            print('ERROR try again')
        else:
            return n3