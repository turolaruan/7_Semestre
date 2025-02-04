import random

def seed():
    random.seed(10)
    
def cria_matriz():
    matriz = []
    seed()
    for i in range(12):
        linha = []
        for j in range(12):
            linha.append(random.randint(0,10))
        matriz.append(linha)
    return matriz

def exibir_matriz(matriz):
    print("Matriz criada: ")
    for linha in matriz:
        print(" ".join(["%3d" % i for i in linha]))

def calcular_operacao(matriz, operacao):
    soma = 0
    contador = 0
    for i in range(12):
        for j in range(12):
            if i+j < 11:
                soma += matriz[i][j]
                contador += 1
    if operacao == "S":
        return soma
    elif operacao == "M":
        return soma/contador

matriz = cria_matriz()
operacao = input("Digite S(Soma) ou M(Média): ")
print(operacao)
exibir_matriz(matriz)
resultado = calcular_operacao(matriz, operacao)
print("Resultado da conta: %.1f" % resultado)



