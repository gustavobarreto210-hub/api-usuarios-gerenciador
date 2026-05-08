from fastapi import FastAPI, HTTPException, status, Response
from pydantic import BaseModel
import uuid

app = FastAPI()

class Usuario(BaseModel):
    nome: str
    email: str
    idade: int

usuarios = []

# 🔍 GET - listar todos
@app.get("/usuarios", status_code=status.HTTP_200_OK)
def listar_usuarios():
    if not usuarios:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return usuarios

# 🔍 GET - buscar por id
@app.get("/usuarios/{usuario_id}", status_code=status.HTTP_200_OK)
def buscar_usuario(usuario_id: str):
    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            return usuario
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuário não encontrado"
    )

# ➕ POST - criar
@app.post("/usuarios", status_code=status.HTTP_201_CREATED)
def criar_usuario(usuario: Usuario):

    for u in usuarios:
        if u["email"] == usuario.email:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email já cadastrado"
            )

    novo_usuario = usuario.dict()
    novo_usuario["id"] = str(uuid.uuid4())

    usuarios.append(novo_usuario)
    return novo_usuario
# ✏️ PUT - atualizar
@app.put("/usuarios/{usuario_id}")
def atualizar_usuario(usuario_id: str, dados: Usuario):
    for usuario in usuarios:
        if usuario["id"] == usuario_id:

            # 🔍 verifica se não houve alteração
            if (
                usuario["nome"] == dados.nome and
                usuario["email"] == dados.email and
                usuario["idade"] == dados.idade
            ):
                return Response(status_code=status.HTTP_204_NO_CONTENT)

            usuario["nome"] = dados.nome
            usuario["email"] = dados.email
            usuario["idade"] = dados.idade

            return usuario  # 200 OK

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuário não encontrado"
    )

# ❌ DELETE - remover
@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: str):
    for index, usuario in enumerate(usuarios):
        if usuario["id"] == usuario_id:
            usuarios.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuário não encontrado"
    )
