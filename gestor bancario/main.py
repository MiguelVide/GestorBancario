import cliente
import bancario
from utils import validar_idade, validar_nif, validar_email, validar_data, calcular_idade

# ==============================
# Cores e estilo
# ==============================
RESET = "\033[0m"
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
AZUL = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"

def linha(char="-", cor=CYAN):
    print(cor + char*60 + RESET)

# ==============================
# MENUS
# ==============================
def menu_principal():
    linha("=", AZUL)
    print(BOLD + AZUL + "🏦 SISTEMA GESTOR BANCÁRIO" + RESET)
    linha("=", AZUL)
    print("1️⃣  Gerir Bancários")
    print("2️⃣  Gerir Clientes")
    print("0️⃣  Sair")
    linha("=", AZUL)

def menu_bancarios():
    linha(char="~", cor=MAGENTA)
    print(BOLD + MAGENTA + "🏦 GESTÃO DE BANCÁRIOS" + RESET)
    print("1️⃣  Criar")
    print("2️⃣  Listar")
    print("3️⃣  Atualizar")
    print("4️⃣  Remover")
    print("5️⃣  Consultar")
    print("0️⃣  Voltar")
    linha(char="~", cor=MAGENTA)

def menu_clientes():
    linha(char="*", cor=AMARELO)
    print(BOLD + AMARELO + "👤 GESTÃO DE CLIENTES" + RESET)
    print("1️⃣  Criar")
    print("2️⃣  Listar")
    print("3️⃣  Atualizar")
    print("4️⃣  Remover")
    print("5️⃣  Consultar")
    print("0️⃣  Voltar")
    linha(char="*", cor=AMARELO)

# ==============================
# Funções auxiliares de input e validação
# ==============================
def input_idade():
    while True:
        try:
            idade = int(input("Idade: "))
            if idade < 18:
                print(VERMELHO + "❌ Menor de idade. Apenas maiores de 18 anos são permitidos." + RESET)
            else:
                return idade
        except ValueError:
            print(VERMELHO + "❌ Idade inválida. Digite um número inteiro." + RESET)

def input_data_nascimento(idade):
    while True:
        data = input("Data de Nascimento (YYYY-MM-DD): ")
        valido, msg = validar_data(data)
        if not valido:
            print(VERMELHO + msg + RESET)
            continue
        valido, msg = validar_idade(idade, data)
        if not valido:
            print(VERMELHO + msg + RESET)
            continue
        return data

def input_nif():
    while True:
        nif = input("NIF: ")
        valido, msg = validar_nif(nif)
        if valido:
            return nif
        print(VERMELHO + msg + RESET)

def input_email():
    while True:
        email = input("Email: ")
        valido, msg = validar_email(email)
        if valido:
            return email
        print(VERMELHO + msg + RESET)

# ==============================
# Gestão Bancários
# ==============================
def gerir_bancarios():
    while True:
        menu_bancarios()
        op = input("👉 Opção: ")
        try:
            if op=="1":  # Criar
                print(VERDE + "Criar Bancário" + RESET)
                nome = input("Nome: ")
                idade = input_idade()
                data_nasc = input_data_nascimento(idade)
                nif = input_nif()
                email = input_email()
                morada = input("Morada: ")
                id_bancario = bancario.criar_bancario(nome, idade, nif, email, morada, data_nasc)
                print(VERDE + f"✅ Bancário criado | ID: {id_bancario}" + RESET)

            elif op=="2":  # Listar
                bancario.listar_bancarios()

            elif op=="3":  # Atualizar
                idb = int(input("ID: "))
                nome = input("Novo nome: ") or None
                idade = input("Nova idade: ")
                idade = int(idade) if idade else None
                data_nasc = input("Nova data de nascimento (YYYY-MM-DD): ") or None
                nif = input("Novo NIF: ") or None
                email = input("Novo email: ") or None
                morada = input("Nova morada: ") or None
                bancario.atualizar_bancario(idb, nome, idade, nif, email, morada, data_nasc)

            elif op=="4":  # Remover
                idb = int(input("ID: "))
                bancario.remover_bancario(idb)

            elif op=="5":  # Consultar
                idb = int(input("ID do Bancário para consultar: "))
                if idb in bancario.bancarios:
                    b = bancario.bancarios[idb]
                    print(MAGENTA + f"""
=============================
ID: {idb}
Nome: {b['nome']}
Idade: {b['idade']}
NIF: {b['nif']}
Email: {b['email']}
Morada: {b['morada']}
Data de Nascimento: {b['data_nascimento']}
=============================
""" + RESET)
                else:
                    print(VERMELHO + "❌ Bancário não encontrado" + RESET)

            elif op=="0":
                break
            else:
                print(VERMELHO + "❌ Opção inválida" + RESET)
        except ValueError:
            print(VERMELHO + "❌ Erro de input" + RESET)

# ==============================
# Gestão Clientes
# ==============================
def gerir_clientes():
    while True:
        menu_clientes()
        op = input("👉 Opção: ")
        try:
            if op=="1":  # Criar
                if not bancario.bancarios:
                    print(AMARELO + "⚠️ Nenhum bancário. Crie um primeiro!" + RESET)
                    gerir_bancarios()
                    continue

                print(CYAN + "📋 LISTA DE BANCÁRIOS DISPONÍVEIS" + RESET)
                for i, b in bancario.bancarios.items():
                    print(f"ID: {i} | Nome: {b['nome']} | Idade: {b['idade']} | Nascimento: {b['data_nascimento']}")

                while True:
                    idb = int(input("ID do Bancário responsável: "))
                    if bancario.existe_bancario(idb):
                        break
                    print(VERMELHO + "❌ ID inválido" + RESET)

                print(VERDE + "Criar Cliente" + RESET)
                nome = input("Nome: ")
                idade = input_idade()
                data_nasc = input_data_nascimento(idade)
                nif = input_nif()
                email = input_email()
                morada = input("Morada: ")
                trabalho = input("Trabalho: ")
                id_cliente = cliente.criar_cliente(nome, idade, nif, email, morada, trabalho, data_nasc, idb)
                print(VERDE + f"✅ Cliente criado | ID: {id_cliente}" + RESET)

            elif op=="2":  # Listar
                cliente.listar_clientes()

            elif op=="3":  # Atualizar
                idc = int(input("ID: "))
                nome = input("Nome: ") or None
                idade = input("Idade: ")
                idade = int(idade) if idade else None
                data_nasc = input("Data de Nascimento (YYYY-MM-DD): ") or None
                nif = input("NIF: ") or None
                email = input("Email: ") or None
                morada = input("Morada: ") or None
                trabalho = input("Trabalho: ") or None
                idb_input = input("ID Bancário: ")
                idb = int(idb_input) if idb_input else None
                if idb and not bancario.existe_bancario(idb):
                    print(VERMELHO + "❌ ID bancário inválido" + RESET)
                    idb = None
                cliente.atualizar_cliente(idc, nome, idade, nif, email, morada, trabalho, data_nasc, idb)

            elif op=="4":  # Remover
                idc = int(input("ID: "))
                cliente.remover_cliente(idc)

            elif op=="5":  # Consultar
                idc = int(input("ID do Cliente para consultar: "))
                if idc in cliente.clientes:
                    c = cliente.clientes[idc]
                    print(AMARELO + f"""
=============================
ID: {idc}
Nome: {c['nome']}
Idade: {c['idade']}
NIF: {c['nif']}
Email: {c['email']}
Morada: {c['morada']}
Trabalho: {c['trabalho']}
Data de Nascimento: {c['data_nascimento']}
Bancário Responsável ID: {c['bancario_id']}
=============================
""" + RESET)
                else:
                    print(VERMELHO + "❌ Cliente não encontrado" + RESET)

            elif op=="0":
                break
            else:
                print(VERMELHO + "❌ Opção inválida" + RESET)

        except ValueError:
            print(VERMELHO + "❌ Erro de input" + RESET)

# ==============================
# MAIN
# ==============================
def main():
    while True:
        menu_principal()
        op = input("👉 Opção: ")
        if op=="1":
            gerir_bancarios()
        elif op=="2":
            gerir_clientes()
        elif op=="0":
            print(VERDE + "👋 Sistema encerrado." + RESET)
            break
        else:
            print(VERMELHO + "❌ Opção inválida" + RESET)

if __name__=="__main__":
    main()