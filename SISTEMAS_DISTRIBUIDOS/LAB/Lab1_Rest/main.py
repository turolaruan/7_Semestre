from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
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
