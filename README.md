# 🏦 Sistema de Gestão Bancária

Sistema de gestão bancária desenvolvido em Python, com suporte a operações CRUD para bancários, clientes, bancos e contas bancárias.

---

## 📁 Estrutura do Projeto

```
├── main.py            # Ponto de entrada da aplicação (menus e interface)
├── bancario.py        # Módulo de gestão de bancários
├── cliente.py         # Módulo de gestão de clientes
├── banco.py           # Módulo de gestão de bancos
├── conta_bancaria.py  # Módulo de gestão de contas bancárias
└── utils.py           # Utilitários (geração de IDs, validações)
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior

### Execução

```bash
python main.py
```

---

## 📋 Funcionalidades

### 👤 Bancários
- Criar, listar, consultar, atualizar e remover bancários
- Validação de NIF (9 dígitos), email e data de nascimento

### 🧑‍💼 Clientes
- Criar, listar, consultar, atualizar e remover clientes
- Associação obrigatória a um bancário responsável
- Validação de idade (mínimo 18 anos) com verificação contra data de nascimento

### 🏛️ Bancos
- Criar, listar, consultar, atualizar e remover bancos
- Validação de NIB (21 dígitos) e email únicos
- Proteção contra remoção de bancos com contas associadas

### 💳 Contas Bancárias
- Criar, listar, consultar, atualizar e remover contas
- Tipos suportados: `corrente` e `poupança`
- Associação a um cliente e a um banco existentes
- Validação de saldo inicial (valor numérico não negativo)

---

## 🔧 Utilitários (`utils.py`)

| Função | Descrição |
|---|---|
| `gerar_id_bancario()` | Gera IDs no formato `B001`, `B002`, ... |
| `gerar_id_cliente()` | Gera IDs no formato `C001`, `C002`, ... |
| `gerar_id_banco()` | Gera IDs no formato `BN001`, `BN002`, ... |
| `gerar_id_conta()` | Gera IDs no formato `CT001`, `CT002`, ... |
| `validar_data(data)` | Valida formato `YYYY-MM-DD` |
| `validar_nif(nif)` | Valida NIF com 9 dígitos numéricos |
| `validar_email(email)` | Valida formato básico de email |
| `validar_idade(idade, data_nasc)` | Valida maioridade e correspondência com data |

---

## 📦 Módulos e Funções

### `bancario.py`
```python
criar_bancario(nome, nif, email, morada, data_nascimento)  → (201, obj) | (400, erro)
listar_bancarios()                                          → (200, dict) | (404, erro)
consultar_bancario(id_bancario)                            → (200, dict) | (404, erro)
atualizar_bancario(id_bancario, ...)                       → (200, obj)  | (400/404, erro)
remover_bancario(id_bancario)                              → (200, msg)  | (404, erro)
existe_bancario(id_bancario)                               → bool
```

### `cliente.py`
```python
criar_cliente(nome, idade, nif, email, morada, trabalho, data_nascimento, id_bancario)
listar_clientes()
consultar_cliente(id_cliente)
atualizar_cliente(id_cliente, ...)
remover_cliente(id_cliente)
```

### `banco.py`
```python
criar_banco(nome, nib, email, morada, telefone)
listar_bancos()
consultar_banco(id_banco)
atualizar_banco(id_banco, ...)
remover_banco(id_banco)
existe_banco(id_banco)
```

### `conta_bancaria.py`
```python
criar_conta(tipo, saldo_inicial, id_cliente, id_banco)
listar_contas()
consultar_conta(id_conta)
atualizar_conta(id_conta, ...)
remover_conta(id_conta)
```

---

## 🔁 Códigos de Resposta

| Código | Significado |
|---|---|
| `200` | Operação realizada com sucesso |
| `201` | Recurso criado com sucesso |
| `400` | Dados inválidos |
| `404` | Recurso não encontrado |
| `409` | Conflito (duplicado) |

---

## ⚠️ Notas

- Os dados são armazenados **em memória** — não há persistência entre execuções.
- Não é possível remover um banco que tenha contas bancárias associadas.
- A idade do cliente é validada contra a data de nascimento fornecida.



