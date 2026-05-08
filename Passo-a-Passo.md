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

