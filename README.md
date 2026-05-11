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

# 🔄 Status Codes Utilizados

### 🔍 GET /usuarios

* `200 OK` → lista de usuários retornada
* `204 No Content` → lista vazia

---

### 🔍 GET /usuarios/{id}

* `200 OK` → usuário encontrado
* `404 Not Found` → usuário não encontrado

---

### ➕ POST /usuarios

* `201 Created` → usuário criado com sucesso

---

### ✏️ PUT /usuarios/{id}

* `200 OK` → usuário atualizado
* `204 No Content` → nenhuma alteração realizada
* `404 Not Found` → usuário não encontrado

---

### ❌ DELETE /usuarios/{id}

* `204 No Content` → usuário removido
* `404 Not Found` → usuário não encontrado

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

# 📄 Sistema de Logs

A API possui um sistema de logging para registrar eventos importantes durante a execução, permitindo melhor monitoramento e depuração.

---

## 🧠 Objetivo

Registrar:

* Requisições realizadas
* Ações importantes (criação, atualização, remoção)
* Erros e situações inesperadas

---

## ⚙️ Configuração

O logger foi configurado utilizando o módulo padrão `logging` do Python:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
    filemode="a"
)

logger = logging.getLogger(__name__)
```

---

## 📊 Níveis de Log Utilizados

* `INFO` → ações normais da aplicação
* `WARNING` → situações inesperadas (ex: usuário não encontrado)

---

## 📌 Exemplos de Logs

```text
2026-05-11 12:00:00 - INFO - Criando usuário com email: teste@email.com
2026-05-11 12:01:00 - INFO - Usuário criado com ID: 123
2026-05-11 12:02:00 - WARNING - Usuário não encontrado: 456
```

---

## 📁 Arquivo de Log

Os logs são armazenados no arquivo:

```
app.log
```

---

## 🚫 Observação

O arquivo `app.log` está listado no `.gitignore` e não é enviado para o repositório, pois contém informações de execução da aplicação.

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
app.log
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

