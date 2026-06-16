from sqlalchemy import Column, String, Date
from app.database import Base


class UsuarioModel(Base):
    __tablename__ = "usuarios"

    id = Column(String, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    data_nascimento = Column(Date, nullable=False)