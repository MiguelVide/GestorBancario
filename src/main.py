import bancario
from bancario import (
    criar_bancario,
    listar_bancarios,
    consultar_bancario,
    atualizar_bancario,
    remover_bancario
)

from cliente import (
    criar_cliente,
    listar_clientes,
    consultar_cliente,
    atualizar_cliente,
    remover_cliente
)

from banco import (
    criar_banco,
    listar_bancos,
    consultar_banco,
    atualizar_banco,
    remover_banco,
    existe_banco
)

from conta_bancaria import (
    criar_conta,
    listar_contas,
    consultar_conta,
    atualizar_conta,
    remover_conta
)

# ==============================
# MENUS
# ==============================
def menu_principal():
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Gerir Bancários")
    print("2 - Gerir Clientes")
    print("3 - Gerir Bancos")
    print("4 - Gerir Contas Bancárias")
    print("0 - Sair")


def menu_bancarios():
    print("\n===== MENU BANCÁRIO =====")
    print("1 - Criar bancário")
    print("2 - Listar bancários")
    print("3 - Consultar bancário")
    print("4 - Atualizar bancário")
    print("5 - Remover bancário")
    print("0 - Voltar")


def menu_clientes():
    print("\n===== MENU CLIENTE =====")
    print("1 - Criar cliente")
    print("2 - Listar clientes")
    print("3 - Consultar cliente")
    print("4 - Atualizar cliente")
    print("5 - Remover cliente")
    print("0 - Voltar")


def menu_bancos():
    print("\n===== MENU BANCO =====")
    print("1 - Criar banco")
    print("2 - Listar bancos")
    print("3 - Consultar banco")
    print("4 - Atualizar banco")
    print("5 - Remover banco")
    print("0 - Voltar")


def menu_contas():
    print("\n===== MENU CONTA BANCÁRIA =====")
    print("1 - Criar conta")
    print("2 - Listar contas")
    print("3 - Consultar conta")
    print("4 - Atualizar conta")
    print("5 - Remover conta")
    print("0 - Voltar")


# ==============================
# FUNÇÃO AUXILIAR (NOVA)
# ==============================
def mostrar_opcoes_ids(dados, tipo):
    print(f"\n--- {tipo} disponíveis ---")
    for id_, info in dados.items():
        print(f"ID: {id_} | Nome: {info['nome']}")
    print("--------------------------\n")


# ==============================
# BANCÁRIOS
# ==============================
def gerir_bancarios():
    while True:
        menu_bancarios()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            nif = input("NIF: ")
            email = input("Email: ")
            morada = input("Morada: ")
            data_nascimento = input("Data nascimento (YYYY-MM-DD): ")

            code, obj = criar_bancario(nome, nif, email, morada, data_nascimento)

            print("✔ Criado" if code == 201 else "Erro:", obj)

        elif opcao == "2":
            code, obj = listar_bancarios()

            if code == 200:
                for id_b, d in obj.items():
                    print(f"{id_b} | {d['nome']} | {d['email']}")
            else:
                print(obj)

        elif opcao == "3":
            bancarios = listar_bancarios()[1]
            if isinstance(bancarios, dict):
                mostrar_opcoes_ids(bancarios, "Bancários")

            id_b = input("ID do bancário: ")
            code, obj = consultar_bancario(id_b)
            print(obj)

        elif opcao == "4":
            bancarios = listar_bancarios()[1]
            if isinstance(bancarios, dict):
                mostrar_opcoes_ids(bancarios, "Bancários")

            id_b = input("ID do bancário: ")

            nome = input("Nome: ")
            nif = input("NIF: ")
            email = input("Email: ")
            morada = input("Morada: ")
            data_nascimento = input("Data nascimento: ")

            code, obj = atualizar_bancario(
                id_b,
                nome or None,
                nif or None,
                email or None,
                morada or None,
                data_nascimento or None
            )

            print(obj)

        elif opcao == "5":
            bancarios = listar_bancarios()[1]
            if isinstance(bancarios, dict):
                mostrar_opcoes_ids(bancarios, "Bancários")

            id_b = input("ID do bancário: ")
            print(remover_bancario(id_b)[1])

        elif opcao == "0":
            break


# ==============================
# CLIENTES
# ==============================
def gerir_clientes():
    while True:
        menu_clientes()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            bancarios = listar_bancarios()[1]
            if isinstance(bancarios, dict):
                mostrar_opcoes_ids(bancarios, "Bancários")

            id_b = input("ID bancário responsável: ")

            nome = input("Nome: ")
            nif = input("NIF: ")
            email = input("Email: ")
            morada = input("Morada: ")
            trabalho = input("Trabalho: ")
            data_nascimento = input("Data nascimento: ")

            print(criar_cliente(nome, nif, email, morada, trabalho, data_nascimento, id_b)[1])

        elif opcao == "2":
            clientes = listar_clientes()[1]

            if isinstance(clientes, dict):
                for id_c, d in clientes.items():
                    print(f"{id_c} | {d['nome']}")
            else:
                print(clientes)

        elif opcao == "3":
            clientes = listar_clientes()[1]
            if isinstance(clientes, dict):
                mostrar_opcoes_ids(clientes, "Clientes")

            id_c = input("ID cliente: ")
            print(consultar_cliente(id_c)[1])

        elif opcao == "4":
            clientes = listar_clientes()[1]
            if isinstance(clientes, dict):
                mostrar_opcoes_ids(clientes, "Clientes")

            id_c = input("ID cliente: ")

            print(atualizar_cliente(
                id_c,
                input("Nome: ") or None,
                input("NIF: ") or None,
                input("Email: ") or None,
                input("Morada: ") or None,
                input("Trabalho: ") or None,
                input("Data nascimento: ") or None,
                input("ID bancário: ") or None
            )[1])

        elif opcao == "5":
            clientes = listar_clientes()[1]
            if isinstance(clientes, dict):
                mostrar_opcoes_ids(clientes, "Clientes")

            id_c = input("ID cliente: ")
            print(remover_cliente(id_c)[1])

        elif opcao == "0":
            break


# ==============================
# BANCOS
# ==============================
def gerir_bancos():
    while True:
        menu_bancos()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            morada = input("Morada: ")
            telefone = input("Telefone: ")

            print(criar_banco(nome, email, morada, telefone)[1])

        elif opcao == "2":
            bancos = listar_bancos()[1]
            if isinstance(bancos, dict):
                for id_b, d in bancos.items():
                    print(f"{id_b} | {d['nome']}")
            else:
                print(bancos)

        elif opcao == "3":
            bancos = listar_bancos()[1]
            if isinstance(bancos, dict):
                mostrar_opcoes_ids(bancos, "Bancos")

            id_bn = input("ID banco: ")
            print(consultar_banco(id_bn)[1])

        elif opcao == "4":
            bancos = listar_bancos()[1]
            if isinstance(bancos, dict):
                mostrar_opcoes_ids(bancos, "Bancos")

            id_bn = input("ID banco: ")

            print(atualizar_banco(
                id_bn,
                input("Nome: ") or None,
                input("Email: ") or None,
                input("Morada: ") or None,
                input("Telefone: ") or None
            )[1])

        elif opcao == "5":
            bancos = listar_bancos()[1]
            if isinstance(bancos, dict):
                mostrar_opcoes_ids(bancos, "Bancos")

            id_bn = input("ID banco: ")
            print(remover_banco(id_bn)[1])

        elif opcao == "0":
            break


# ==============================
# CONTAS
# ==============================
def gerir_contas():
    while True:
        menu_contas()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            clientes = listar_clientes()[1]
            if isinstance(clientes, dict):
                mostrar_opcoes_ids(clientes, "Clientes")

            id_c = input("ID cliente: ")

            bancos = listar_bancos()[1]
            if isinstance(bancos, dict):
                mostrar_opcoes_ids(bancos, "Bancos")

            id_b = input("ID banco: ")

            tipo = input("Tipo: ")
            saldo = float(input("Saldo: "))

            print(criar_conta(tipo, saldo, id_c, id_b)[1])

        elif opcao == "2":
            contas = listar_contas()[1]

            if isinstance(contas, dict):
                for id_ct, d in contas.items():
                    print(f"{id_ct} | {d['tipo']} | {d['saldo']}")
            else:
                print(contas)

        elif opcao == "3":
            contas = listar_contas()[1]
            if isinstance(contas, dict):
                mostrar_opcoes_ids(contas, "Contas")

            id_ct = input("ID conta: ")
            print(consultar_conta(id_ct)[1])

        elif opcao == "4":
            contas = listar_contas()[1]
            if isinstance(contas, dict):
                mostrar_opcoes_ids(contas, "Contas")

            id_ct = input("ID conta: ")

            print(atualizar_conta(
                id_ct,
                input("Tipo: ") or None,
                input("Saldo: ") or None,
                input("ID cliente: ") or None,
                input("ID banco: ") or None
            )[1])

        elif opcao == "5":
            contas = listar_contas()[1]
            if isinstance(contas, dict):
                mostrar_opcoes_ids(contas, "Contas")

            id_ct = input("ID conta: ")
            print(remover_conta(id_ct)[1])

        elif opcao == "0":
            break


# ==============================
# MAIN
# ==============================
def main():
    while True:
        menu_principal()
        opcao = input("Escolha: ")

        if opcao == "1":
            gerir_bancarios()
        elif opcao == "2":
            gerir_clientes()
        elif opcao == "3":
            gerir_bancos()
        elif opcao == "4":
            gerir_contas()
        elif opcao == "0":
            break


if __name__ == "__main__":
    main()
