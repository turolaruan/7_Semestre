import random

def lanca_dados():
    return random.randint(1,6) + random.randint(1,6)

def main():
    resultados = {}
    for i in range(1000):
        resultado = lanca_dados()
        if resultado in resultados:
            resultados[resultado] += 1
        else:
            resultados[resultado] = 1
    for resultado in sorted(resultados.keys()):
        print("Resultado: %d - Frequência: %.2f%%" % (resultado, (resultados[resultado] / 1000) * 100))

main()