from fastapi import APIRouter, HTTPException, status, Response, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import uuid
import logging
from datetime import date

from app.database import get_db
from app.models import UsuarioModel
from app.schemas import Usuario, UsuarioResponse

logger = logging.getLogger(__name__)

router = APIRouter()


def calcular_idade(data_nascimento: date) -> int:
    hoje = date.today()
    idade = hoje.year - data_nascimento.year

    if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1

    return idade


@router.get("/usuarios", status_code=status.HTTP_200_OK)
def listar_usuarios(db: Session = Depends(get_db)):
    logger.info("Requisição para listar usuários")

    usuarios = db.query(UsuarioModel).all()

    if not usuarios:
        logger.info("Nenhum usuário encontrado")
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return usuarios


@router.get("/usuarios/{usuario_id}", response_model=UsuarioResponse)
def buscar_usuario(usuario_id: str, db: Session = Depends(get_db)):
    logger.info(f"Buscando usuário ID: {usuario_id}")

    usuario = db.query(UsuarioModel).filter(
        UsuarioModel.id == usuario_id
    ).first()

    if not usuario:
        logger.warning(f"Usuário não encontrado: {usuario_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado"
        )

    return usuario


@router.post(
    "/usuarios",
    status_code=status.HTTP_201_CREATED,
    response_model=UsuarioResponse
)
def criar_usuario(usuario: Usuario, db: Session = Depends(get_db)):
    logger.info(f"Tentando criar usuário com email: {usuario.email}")

    idade = calcular_idade(usuario.data_nascimento)

    if idade < 18:
        logger.warning("Tentativa de cadastro de menor de idade")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Apenas acima de 18 anos é permitido"
        )

    usuario_existente = db.query(UsuarioModel).filter(
        UsuarioModel.email == usuario.email
    ).first()

    if usuario_existente:
        logger.warning(f"Email já cadastrado: {usuario.email}")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email já cadastrado"
        )

    novo_usuario = UsuarioModel(
        id=str(uuid.uuid4()),
        nome=usuario.nome,
        email=usuario.email,
        data_nascimento=usuario.data_nascimento
    )

    try:
        db.add(novo_usuario)
        db.commit()
        db.refresh(novo_usuario)

        logger.info(f"Usuário criado com ID: {novo_usuario.id}")

        return novo_usuario

    except SQLAlchemyError:
        db.rollback()
        logger.error("Erro ao salvar usuário no banco de dados")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao salvar usuário no banco de dados"
        )


@router.put("/usuarios/{usuario_id}", response_model=UsuarioResponse)
def atualizar_usuario(
    usuario_id: str,
    dados: Usuario,
    db: Session = Depends(get_db)
):
    logger.info(f"Tentando atualizar usuário ID: {usuario_id}")

    idade = calcular_idade(dados.data_nascimento)

    if idade < 18:
        logger.warning("Tentativa de atualização para menor de idade")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Apenas acima de 18 anos é permitido"
        )

    usuario = db.query(UsuarioModel).filter(
        UsuarioModel.id == usuario_id
    ).first()

    if not usuario:
        logger.warning(f"Usuário não encontrado para atualização: {usuario_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado"
        )

    if (
        usuario.nome == dados.nome
        and usuario.email == dados.email
        and usuario.data_nascimento == dados.data_nascimento
    ):
        logger.info(f"Nenhuma alteração para usuário ID: {usuario_id}")
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    try:
        usuario.nome = dados.nome
        usuario.email = dados.email
        usuario.data_nascimento = dados.data_nascimento

        db.commit()
        db.refresh(usuario)

        logger.info(f"Usuário atualizado: {usuario_id}")

        return usuario

    except SQLAlchemyError:
        db.rollback()
        logger.error(f"Erro ao atualizar usuário ID: {usuario_id}")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao atualizar usuário no banco de dados"
        )


@router.delete("/usuarios/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_usuario(usuario_id: str, db: Session = Depends(get_db)):
    logger.info(f"Tentando deletar usuário ID: {usuario_id}")

    usuario = db.query(UsuarioModel).filter(
        UsuarioModel.id == usuario_id
    ).first()

    if not usuario:
        logger.warning(f"Usuário não encontrado para deleção: {usuario_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado"
        )

    try:
        db.delete(usuario)
        db.commit()

        logger.info(f"Usuário deletado: {usuario_id}")

        return Response(status_code=status.HTTP_204_NO_CONTENT)

    except SQLAlchemyError:
        db.rollback()
        logger.error(f"Erro ao deletar usuário ID: {usuario_id}")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao deletar usuário no banco de dados"
        )