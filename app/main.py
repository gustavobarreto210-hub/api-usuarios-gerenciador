from fastapi import FastAPI
import logging

from app.database import Base, engine
from app.routes import router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
    filemode="a",
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Gerenciamento de Usuários",
    description="API com FastAPI, PostgreSQL, SQLAlchemy e Podman.",
    version="2.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {"mensagem": "API de Gerenciamento de Usuários funcionando!"}