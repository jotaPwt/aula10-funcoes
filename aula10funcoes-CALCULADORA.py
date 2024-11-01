# def saudacoes(nome):
#     print(nome)

# saudacoes('Joao')

# def idade():
#     print(25)

# idade()

print('============== CALCULADORA ==============')

def soma():
    print('SOMA')
    n1 = int(input('Digite um numero'))
    n2 = int(input('Digite um numero'))
    soma = n1 + n2
    print(soma)
    
def sub():
    print('SUBTRAÇÃO')
    n1 = int(input('Digite um numero'))
    n2 = int(input('Digite um numero'))
    sub = n1 - n2
    print(sub)


def div():
    print('DIVISÃO')
    n1 = int(input('Digite um numero >>'))
    n2 = int(input('Digite um numero >>'))
    div = n1 // n2
    print(div)


def mult():
    print('MULTIPLICAÇÃO')
    n1 = int(input('Digite um numero >>'))
    n2 = int(input('Digite um numero >>'))
    mult = n1 * n2
    print(mult)



def calculo():
    escolha = input('Escolha seu calculo, +, /, -, * >>')
    
    if escolha == '+':
        soma()
    elif escolha == '/':
        div()
    elif escolha == '-':
        sub()
    elif escolha == '*':
        mult()
    else:
        print('Digitação incorreta')
    
# calculo

loop = True

while True:

    deseja = input('Deseja fazer uma operação? s/n >>')

    while deseja == 's':
        calculo()
        break
    else:
        print('Você saiu')
        break
else:
    print('Você saiue')