import grpc
import calculadora_pb2
import calculadora_pb2_grpc

print("Cliente conectando com servidor")

porta = "50051"
endereco = "localhost"

with grpc.insecure_channel(f"{endereco}:{porta}") as channel:
    stub = calculadora_pb2_grpc.CalcStub(channel)
    while True:
        print("1 - Soma")
        print("2 - Subtracao")
        print("3 - Multiplicacao")
        print("4 - Divisao")
        print("5 - Sair")
        operacao = int(input("Digite a operacao desejada: "))
        if operacao == 1:
            valor1 = float(input("Digite o primeiro valor: "))
            valor2 = float(input("Digite o segundo valor: "))
            resposta = stub.Soma(calculadora_pb2.Valores(valor1=valor1, valor2=valor2))
            print(f"Resultado: {resposta.resultado}")
        elif operacao == 2:
            valor1 = float(input("Digite o primeiro valor: "))
            valor2 = float(input("Digite o segundo valor: "))
            resposta = stub.Subtracao(calculadora_pb2.Valores(valor1=valor1, valor2=valor2))
            print(f"Resultado: {resposta.resultado}")
        elif operacao == 3:
            valor1 = float(input("Digite o primeiro valor: "))
            valor2 = float(input("Digite o segundo valor: "))
            resposta = stub.Multiplicacao(calculadora_pb2.Valores(valor1=valor1, valor2=valor2))
            print(f"Resultado: {resposta.resultado}")
        elif operacao == 4:
            valor1 = float(input("Digite o primeiro valor: "))
            valor2 = float(input("Digite o segundo valor: "))
            resposta = stub.Divisao(calculadora_pb2.Valores(valor1=valor1, valor2=valor2))
            print(f"Resultado: {resposta.resultado}")
        elif operacao == 5:
            break
        else:
            print("Operacao invalida")

        

