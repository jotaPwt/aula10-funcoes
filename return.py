def calc(a, b):
    soma = a + b
    return soma

funcao = calc(100, 2000)
print(funcao)

def sub(a, b):
    return a - b

subtracao = sub(100, 10)
print(subtracao)

def div(a, b):
    div = a / b 
    return div

divisao = div(50, 25)
print(divisao)  

def mult(a, b):
    return a * b

multiplicacao = mult(100, 100)
print(multiplicacao)



def teste():
    lista = [input('>'), input('>'), input('>')]
    return lista

var = teste()
print(var)



def lista(lista):
    media = sum(lista) / len(lista)

lista_notas = [1, 3 , 10]
