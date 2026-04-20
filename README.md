Projeto Gestor Bancário - CRUD Bancário e Cliente


📘 Descrição do Projeto

funções (sem classes)
dicionários
separação por ficheiros
validação de dados
menus em terminal

O projeto simula a gestão de duas entidades relacionadas: Bancário e Cliente.

🎯 Objetivos Pedagógicos
Com este projeto os alunos devem aprender a:

organizar código em múltiplos ficheiros Python
utilizar dicionários como estrutura de armazenamento
implementar operações CRUD para múltiplas entidades
validar dados introduzidos pelo utilizador
gerar identificadores automáticos
trabalhar com datas em Python
separar lógica de negócio da interface (menu)
relacionar entidades (cliente associado a um bancário)


📂 Estrutura do Projeto
.
└── gestor_bancario
     ├── main.py
     ├── bancario.py
     ├── cliente.py
     ├── utils.py
└── README.md
main.py
Contém o menu interativo em terminal.
Responsável apenas por:

apresentar opções
recolher dados do utilizador
chamar funções dos módulos bancario e cliente

Não contém validações.
bancario.py
Contém todas as operações CRUD da entidade Bancário:

criar bancário
listar bancários
consultar bancário
atualizar bancário
remover bancário
verificar existência de bancário (existe_bancario)

Também inclui validações como:

verificação de NIF (9 dígitos)
verificação de email
verificação de data de nascimento
geração automática de ID

Os bancários são guardados num dicionário em memória.
cliente.py
Contém todas as operações CRUD da entidade Cliente:

criar cliente
listar clientes
consultar cliente
atualizar cliente
remover cliente

Também inclui validações como:

verificação de idade mínima (18 anos)
coerência entre idade e data de nascimento
verificação de NIF, email e data
associação obrigatória a um bancário existente

Os clientes são guardados num dicionário em memória.
utils.py
Contém funções auxiliares partilhadas:

geração automática de IDs para bancários (B001, B002, ...)
geração automática de IDs para clientes (C001, C002, ...)
validação de datas no formato YYYY-MM-DD
validação de NIF (9 dígitos numéricos)
validação de email (presença de @ e .)
validação de idade (mínimo 18 anos e coerência com data de nascimento)


👤 Estrutura das Entidades
Bancário
Cada bancário contém:

id_bancario (gerado automaticamente, ex: B001)
nome
nif
email
morada
data_nascimento

Exemplo:
B001
Nome: João Ferreira
NIF: 123456789
Email: joao@banco.pt
Morada: Rua das Flores, Lisboa
Data nascimento: 1985-06-20
Cliente
Cada cliente contém:

id_cliente (gerado automaticamente, ex: C001)
nome
idade
nif
email
morada
trabalho
data_nascimento
bancario_id (referência ao bancário responsável)

Exemplo:
C001
Nome: Ana Silva
Idade: 30
NIF: 987654321
Email: ana@email.pt
Morada: Av. Central, Porto
Trabalho: Engenheira
Data nascimento: 1994-03-12
Bancário ID: B001

▶️ Como Executar o Projeto
1️⃣ Garantir que Python está instalado
2️⃣ Executar no terminal:
python main.py
3️⃣ Utilizar o menu apresentado:
===== MENU PRINCIPAL =====
1 - Gerir Bancários
2 - Gerir Clientes
0 - Sair

⚠️ É necessário criar pelo menos um bancário antes de criar clientes, uma vez que cada cliente deve estar associado a um bancário existente.


🔗 Relação entre Entidades
Bancário  1 ──────── N  Cliente

Um bancário pode ser responsável por vários clientes.
Um cliente está sempre associado a exatamente um bancário.
Ao criar ou atualizar um cliente, o sistema valida se o id_bancario fornecido existe.


📚 Conceitos Trabalhados
Este projeto permite consolidar:

funções
dicionários
módulos Python
importação entre ficheiros
validação de dados
estruturas condicionais
ciclos (while)
relações entre entidades
códigos de retorno (200, 201, 400, 404)


👨‍🏫 Utilização em Sala de Aula
Este projeto vai ser usado para:

introdução ao CRUD com múltiplas entidades
exercícios guiados de validação e relações
avaliação prática
preparação para projetos maiores

