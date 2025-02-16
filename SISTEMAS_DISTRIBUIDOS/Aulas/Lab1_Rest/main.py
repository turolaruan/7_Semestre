from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

"""
tarefas = list() 

class Tarefa(BaseModel): # Classe para definir o modelo de uma tarefa
    tarefa: str
    prioridade: int
    feito: bool

@app.get("/") 
def root():
    return tarefas


@app.get("/tarefa/{pos}") # Retorna a tarefa na posição pos
def get_tarefa(pos: int):
    return tarefas[pos]

@app.post("/adicionar/") # Adiciona uma nova tarefa
def criar_tarefa(tarefa: Tarefa):
    tarefa.feito = False
    tarefas.append(tarefa)
    return len(tarefas)

@app.put("/feito/{pos}") # Marca a tarefa na posição pos como feita
def marcar_feito(pos: int):
    tarefas[pos].feito = True
    return tarefas[pos]

@app.delete("/deletar/{pos}") # Deleta a tarefa na posição pos
def deletar_tarefa(pos: int):
    tarefa = tarefas.pop(pos)
    return tarefa
"""

lista_contatos = list()

class Contato(BaseModel): # Classe para definir o modelo de um contato
    nome: str
    telefone: str
    email: str

@app.get("/") # Retorna a lista de contatos
def root():
    return lista_contatos

@app.get("/contato/{pos}") # Retorna o contato na posição pos
def get_contato(pos: int):
    return lista_contatos[pos]

@app.post("/adicionar/") # Adiciona um novo contato
def criar_contato(contato: Contato):
    lista_contatos.append(contato)
    return len(lista_contatos)

@app.put("/atualizar/{pos}") # Atualiza o contato na posição pos com os novos dados
def atualizar_contato(pos: int, nome: str, telefone: str, email: str):
    lista_contatos[pos].nome = nome
    lista_contatos[pos].telefone = telefone
    lista_contatos[pos].email = email
    return lista_contatos[pos]

@app.delete("/deletar/{pos}") # Deleta o contato na posição pos
def deletar_contato(pos: int):
    contato = lista_contatos.pop(pos)
    return contato 