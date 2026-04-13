Projeto Gestor Bancário - CRUD Bancários e Clientes
📘 Descrição do Projeto
Este projeto foi desenvolvido com fins pedagógicos para alunos do Curso Profissional de Gestão e Programação de Sistemas Informáticos (GPSI) – 10.º ano.

O objetivo principal é demonstrar a implementação de operações CRUD (Create, Read, Update, Delete) e o relacionamento entre entidades em Python utilizando:

funções (sem classes)

dicionários

separação por ficheiros (módulos)

validação de dados rigorosa

menus em terminal com interface colorida

O projeto simula um sistema de gestão onde Bancários são responsáveis pela gestão de Clientes.

🎯 Objetivos Pedagógicos
Com este projeto os alunos devem aprender a:

organizar código complexo em múltiplos ficheiros (modularização)

utilizar dicionários aninhados para armazenamento em memória

implementar a lógica de relacionamento entre duas entidades (ID de Bancário em Cliente)

validar dados técnicos (NIF com 9 dígitos, Email, Datas)

calcular dados dinâmicos (Idade a partir da Data de Nascimento)

separar a interface visual (main) da lógica de manipulação de dados

📂 Estrutura do Projeto
.
└──gestor_bancario
     ├── main.py        (Interface e Menus)
     ├── bancario.py    (CRUD Bancários)
     ├── cliente.py     (CRUD Clientes)
     ├── utils.py       (Validações e Cálculos)
└── README.md
main.py
Contém o menu interativo em terminal.

Responsável por:

Apresentar menus coloridos e organizados.

Recolher inputs do utilizador com validação imediata.

Encaminhar as operações para os módulos respetivos.

bancario.py & cliente.py
Contêm as operações CRUD de cada entidade:

Criar: Registo com geração de ID automático.

Listar: Exibição resumida de todos os registos.

Consultar: Visualização detalhada de um registo específico.

Atualizar: Edição de campos existentes.

Remover: Eliminação de registos do dicionário.

Nota: Um Cliente só pode ser criado se for associado a um Bancário existente.

utils.py
Contém as funções de suporte lógico:

validar_nif: Garante que tem 9 dígitos numéricos.

validar_email: Verifica a presença de "@" e ".".

validar_data: Valida o formato YYYY-MM-DD.

calcular_idade: Calcula a idade real comparando com a data atual.

👤 Estrutura das Entidades
Bancário
Nome, Idade, NIF, Email, Morada, Data Nascimento.

Cliente
Nome, Idade, NIF, Email, Morada, Trabalho, Data Nascimento.

ID Bancário Responsável (Chave de ligação).

▶️ Como Executar o Projeto
1️⃣ Certifica-te que tens todos os ficheiros na mesma pasta.

2️⃣ Executa no terminal:

Bash
python main.py
3️⃣ Segue as instruções nos menus (usa as cores para identificar sucessos ou erros).

📚 Conceitos Trabalhados
Este projeto consolida conhecimentos avançados de:

Módulos e Importação (import).

Relacionamento entre dicionários.

Manipulação do módulo datetime.

Tratamento de erros e exceções (try/except).

Formatação de strings e estilos ANSI (Cores no terminal).

📄 Licença Pedagógica
Projeto desenvolvido exclusivamente para fins educativos no curso GPSI – 10.º ano.

Pode ser reutilizado e adaptado livremente pelo professor e alunos.
