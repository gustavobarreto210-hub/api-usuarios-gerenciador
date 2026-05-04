from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI()


class Usuario(BaseModel):
    nome: str
    idade: int
    email: str


usuarios = []


@app.get("/usuarios")
def listar_usuarios():
    return usuarios


@app.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id: str):
    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado")


@app.post("/usuarios")
def criar_usuario(usuario: Usuario):
    novo_usuario = usuario.dict()
    novo_usuario["id"] = str(uuid.uuid4())
    usuarios.append(novo_usuario)
    return novo_usuario


@app.put("/usuarios/{usuario_id}")
def atualizar_usuario(usuario_id: str, dados: Usuario):
    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            usuario["nome"] = dados.nome
            usuario["email"] = dados.email
            usuario["idade"] = dados.idade
            return usuario

    raise HTTPException(status_code=404, detail="Usuário não encontrado")


@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: str):
    for index, usuario in enumerate(usuarios):
        if usuario["id"] == usuario_id:
            usuarios.pop(index)
            return {"mensagem": "Usuário deletado com sucesso"}

    raise HTTPException(status_code=404, detail="Usuário não encontrado")
