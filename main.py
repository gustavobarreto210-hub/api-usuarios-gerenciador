from fastapi import FastAPI, HTTPException, status, Response
from pydantic import BaseModel
import uuid
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
    filemode="a",
)

logger = logging.getLogger(__name__)

app = FastAPI()


class Usuario(BaseModel):
    nome: str
    email: str
    idade: int


usuarios = []


# 🔍 GET - listar todos
@app.get("/usuarios", status_code=status.HTTP_200_OK)
def listar_usuarios():
    logger.info("Requisição para listar usuários")

    if not usuarios:
        logger.info("Nenhum usuário encontrado")
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return usuarios


# 🔍 GET - buscar por id
@app.get("/usuarios/{usuario_id}", status_code=status.HTTP_200_OK)
def buscar_usuario(usuario_id: str):
    logger.info(f"Buscando usuário ID: {usuario_id}")

    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            logger.info(f"Usuário encontrado: {usuario_id}")
            return usuario

    logger.warning(f"Usuário não encontrado: {usuario_id}")

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado"
    )


# ➕ POST - criar
@app.post("/usuarios", status_code=status.HTTP_201_CREATED)
def criar_usuario(usuario: Usuario):
    logger.info(f"Tentando criar usuário com email: {usuario.email}")

    for u in usuarios:
        if u["email"] == usuario.email:
            logger.warning(f"Email já cadastrado: {usuario.email}")
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Email já cadastrado"
            )

    novo_usuario = usuario.dict()
    novo_usuario["id"] = str(uuid.uuid4())

    usuarios.append(novo_usuario)

    logger.info(f"Usuário criado com ID: {novo_usuario['id']}")

    return novo_usuario


# ✏️ PUT - atualizar
@app.put("/usuarios/{usuario_id}")
def atualizar_usuario(usuario_id: str, dados: Usuario):
    logger.info(f"Tentando atualizar usuário ID: {usuario_id}")

    for usuario in usuarios:
        if usuario["id"] == usuario_id:

            if (
                usuario["nome"] == dados.nome
                and usuario["email"] == dados.email
                and usuario["idade"] == dados.idade
            ):
                logger.info(f"Nenhuma alteração para usuário ID: {usuario_id}")
                return Response(status_code=status.HTTP_204_NO_CONTENT)

            usuario["nome"] = dados.nome
            usuario["email"] = dados.email
            usuario["idade"] = dados.idade

            logger.info(f"Usuário atualizado: {usuario_id}")

            return usuario

    logger.warning(f"Usuário não encontrado para atualização: {usuario_id}")

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado"
    )


# ❌ DELETE - remover
@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: str):
    logger.info(f"Tentando deletar usuário ID: {usuario_id}")

    for index, usuario in enumerate(usuarios):
        if usuario["id"] == usuario_id:
            usuarios.pop(index)

            logger.info(f"Usuário deletado: {usuario_id}")

            return Response(status_code=status.HTTP_204_NO_CONTENT)

    logger.warning(f"Usuário não encontrado para deleção: {usuario_id}")

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado"
    )
