from concurrent import futures
import grpc
import calculadora_pb2
import calculadora_pb2_grpc

class Calc(calculadora_pb2_grpc.CalcServicer):
    def Soma(self, request, context):
        return calculadora_pb2.Resultado(resultado=request.valor1 + request.valor2)
    def Subtracao(self, request, context):
        return calculadora_pb2.Resultado(resultado=request.valor1 - request.valor2)
    def Multiplicacao(self, request, context):
        return calculadora_pb2.Resultado(resultado=request.valor1 * request.valor2)
    def Divisao(self, request, context):
        return calculadora_pb2.Resultado(resultado=request.valor1 / request.valor2)     

endereco = "[::]:50051"
servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
calculadora_pb2_grpc.add_CalcServicer_to_server(Calc(), servidor)

servidor.add_insecure_port(endereco)
servidor.start()
print(f"Servidor escutando em {endereco}")
servidor.wait_for_termination()
