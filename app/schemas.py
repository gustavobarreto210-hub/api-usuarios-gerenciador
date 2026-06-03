from pydantic import BaseModel
from datetime import date


class Usuario(BaseModel):
    nome: str
    email: str
    data_nascimento: date


class UsuarioResponse(BaseModel):
    id: str
    nome: str
    email: str
    data_nascimento: date

    class Config:
        from_attributes = True