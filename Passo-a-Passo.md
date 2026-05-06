# 🚀 API de Usuários com FastAPI

## 📌 Descrição

Esta é uma API RESTful desenvolvida com FastAPI que realiza operações de CRUD (Create, Read, Update, Delete) para gerenciamento de usuários.

Os dados são armazenados em memória e cada usuário possui:

* Nome
* Email
* Idade
* ID único gerado automaticamente (UUID)

---

## 🛠️ Tecnologias utilizadas

* Python 3
* FastAPI
* Uvicorn

---

# ⚙️ Configuração do ambiente

## 🪟 Windows (CMD / PowerShell / Git Bash)

### 1. Entrar na pasta do projeto

```bash
cd Desktop/meu-projeto
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

### 3. Ativar ambiente

* Git Bash:

```bash
source venv/Scripts/activate
```

* PowerShell:

```bash
venv\Scripts\Activate.ps1
```

* CMD:

```bash
venv\Scripts\activate.bat
```

---

## 🐧 Fedora / Linux

### 1. Entrar na pasta do projeto

```bash
cd ~/meu-projeto
```

### 2. Criar ambiente virtual

```bash
python3 -m venv venv
```

### 3. Ativar ambiente

```bash
source venv/bin/activate
```

---

## 📦 Instalar dependências

```bash
pip install fastapi uvicorn
```

---

# 📁 Criando o arquivo da API

## 🪟 Windows (Visual Studio Code)

1. Abra a pasta do projeto no VS Code
2. Clique com botão direito
3. New File
4. Nome:

```
main.py
```

---

## 🐧 Fedora / Linux

```bash
touch main.py
```

ou

```bash
nano main.py
```

---

## 💻 Código inicial

```python
from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()

class Usuario(BaseModel):
    nome: str
    email: str
    idade: int

usuarios = []

@app.get("/usuarios")
def listar_usuarios():
    return usuarios

@app.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id: str):
    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            return usuario
    return {"erro": "Usuário não encontrado"}

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
    return {"erro": "Usuário não encontrado"}

@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: str):
    for index, usuario in enumerate(usuarios):
        if usuario["id"] == usuario_id:
            usuarios.pop(index)
            return {"mensagem": "Usuário deletado"}
    return {"erro": "Usuário não encontrado"}
```

---

# 🚀 Executar a API

```bash
uvicorn main:app --reload
```

---

# 🌐 Testar no navegador

Acesse:

```
http://127.0.0.1:8000/docs
```

---

# 📚 Endpoints

* GET /usuarios
* GET /usuarios/{id}
* POST /usuarios
* PUT /usuarios/{id}
* DELETE /usuarios/{id}

---

# 📦 Exemplo de requisição

```json
{
  "nome": "Gustavo",
  "email": "gustavo@email.com",
  "idade": 25
}
```

---

# ⚠️ Tratamento de erros

* Usuário não encontrado
* Dados inválidos

---

# 🌐 Versionamento com Git e GitHub

## Inicializar repositório

```bash
git init
```

---

## Criar `.gitignore`

```bash
touch .gitignore
```

Conteúdo:

```
venv/
__pycache__/
*.pyc
.env
```

---

## Commit inicial

```bash
git add .
git commit -m "Primeira versão da API"
```

---

## Configurar Git (se necessário)

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@email.com"
```

---

## Conectar ao GitHub

```bash
git remote add origin https://github.com/seu-usuario/seu-repositorio.git
git branch -M main
git push -u origin main
```

---

## Atualizações futuras

```bash
git add .
git commit -m "Atualização"
git push
```

---

# 🛑 Desativar ambiente virtual

```bash
deactivate
```

---

# 💡 Observações finais

* Dados são armazenados em memória
* API segue padrão REST
* Documentação automática via Swagger
* Projeto focado em aprendizado de APIs e Git

---

# 👨‍💻 Autor

Gustavo Gomes

