# PostgreSQL com Podman - Guia de Criação e Manipulação

## Objetivo

Este documento descreve o processo de criação de um container PostgreSQL utilizando Podman e os principais comandos para manipulação do banco de dados.

---

# 1. Criando o Container PostgreSQL

Executar o comando abaixo:

```bash
podman run -d \
  --name postgres-api \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=usuarios_db \
  -p 5432:5432 \
  docker.io/library/postgres:16
```

## Explicação dos parâmetros

| Parâmetro           | Descrição                            |
| ------------------- | ------------------------------------ |
| -d                  | Executa o container em segundo plano |
| --name postgres-api | Nome do container                    |
| POSTGRES_USER       | Usuário do banco                     |
| POSTGRES_PASSWORD   | Senha do banco                       |
| POSTGRES_DB         | Banco criado automaticamente         |
| -p 5432:5432        | Mapeamento da porta PostgreSQL       |
| postgres:16         | Imagem oficial do PostgreSQL         |

---

# 2. Verificar Containers em Execução

```bash
podman ps
```

Exemplo:

```bash
CONTAINER ID   IMAGE        STATUS
abc123         postgres:16  Up 2 minutes
```

---

# 3. Parar o Container

```bash
podman stop postgres-api
```

---

# 4. Iniciar o Container

```bash
podman start postgres-api
```

---

# 5. Reiniciar o Container

```bash
podman restart postgres-api
```

---

# 6. Remover o Container

Primeiro pare o container:

```bash
podman stop postgres-api
```

Depois remova:

```bash
podman rm postgres-api
```

---

# 7. Acessando o PostgreSQL

Entrar no banco:

```bash
podman exec -it postgres-api psql -U postgres -d usuarios_db
```

---

# 8. Comandos Básicos do PostgreSQL

## Listar Bancos

```sql
\l
```

## Conectar em um Banco

```sql
\c usuarios_db
```

## Listar Tabelas

```sql
\dt
```

## Mostrar Estrutura de uma Tabela

```sql
\d usuarios
```

## Mostrar Registros

```sql
SELECT * FROM usuarios;
```

## Buscar Usuário por Email

```sql
SELECT * FROM usuarios
WHERE email = 'gustavo@email.com';
```

## Contar Usuários

```sql
SELECT COUNT(*) FROM usuarios;
```

---

# 9. Inserir Dados Manualmente

```sql
INSERT INTO usuarios (
    id,
    nome,
    email,
    data_nascimento
)
VALUES (
    '123',
    'Gustavo',
    'gustavo@email.com',
    '2000-01-01'
);
```

---

# 10. Atualizar Dados

```sql
UPDATE usuarios
SET nome = 'Gustavo Gomes'
WHERE email = 'gustavo@email.com';
```

---

# 11. Remover Dados

```sql
DELETE FROM usuarios
WHERE email = 'gustavo@email.com';
```

---

# 12. Sair do PostgreSQL

```sql
\q
```

---

# 13. Fluxo Utilizado na API

A API utiliza:

* FastAPI
* SQLAlchemy
* PostgreSQL
* Podman

Os dados não ficam mais armazenados em memória.

Quando um usuário é criado através do endpoint:

```http
POST /usuarios
```

o SQLAlchemy executa:

```python
db.add(novo_usuario)
db.commit()
```

persistindo o registro dentro do PostgreSQL.

Quando um usuário é consultado:

```http
GET /usuarios
```

o SQLAlchemy executa:

```python
db.query(UsuarioModel).all()
```

retornando os dados armazenados no banco.

Dessa forma, mesmo reiniciando a API, os registros permanecem salvos no PostgreSQL.
