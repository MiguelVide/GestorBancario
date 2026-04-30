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

            if code == 201:
                print("Bancário criado com sucesso.")
                print(obj)
            else:
                print("Erro:", obj)

        elif opcao == "2":
            code, obj = listar_bancarios()

            if code == 200:
                for id_b, dados in obj.items():
                    print(f"ID: {id_b} | Nome: {dados['nome']} | NIF: {dados['nif']} | Email: {dados['email']} | Morada: {dados['morada']} | Data Nascimento: {dados['data_nascimento']}")
            else:
                print("Erro:", obj)

        elif opcao == "3":
            id_b = input("ID do bancário: ")
            code, obj = consultar_bancario(id_b)

            if code == 200:
                print(obj[id_b])
                print("Bancário consultado com sucesso.")
            else:
                print("Erro:", obj)

        elif opcao == "4":
            id_b = input("ID do bancário: ")

            nome = input("Novo nome (enter para manter): ")
            nif = input("Novo NIF (enter para manter): ")
            email = input("Novo email (enter para manter): ")
            morada = input("Nova morada (enter para manter): ")
            data_nascimento = input("Nova data nascimento YYYY-MM-DD (enter para manter): ")

            code, obj = atualizar_bancario(
                id_b,
                nome if nome else None,
                nif if nif else None,
                email if email else None,
                morada if morada else None,
                data_nascimento if data_nascimento else None
            )

            if code == 200:
                print("Bancário atualizado com sucesso.")
            else:
                print("Erro:", obj)

        elif opcao == "5":
            id_b = input("ID do bancário: ")
            code, obj = remover_bancario(id_b)

            if code == 200:
                print(obj)
            else:
                print("Erro:", obj)

        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


# ==============================
# CLIENTES
# ==============================
def gerir_clientes():
    while True:
        menu_clientes()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            code, obj = listar_bancarios()

            if code != 200:
                print("Não existem bancários. Crie primeiro.")
                continue

            id_b = input("ID do bancário responsável: ")

            if not bancario.existe_bancario(id_b):
                print("Erro: ID de bancário inválido.")
                continue

            nome = input("Nome: ")
            idade = int(input("Idade: "))
            nif = input("NIF: ")
            email = input("Email: ")
            morada = input("Morada: ")
            trabalho = input("Trabalho: ")
            data_nascimento = input("Data nascimento (YYYY-MM-DD): ")

            code, obj = criar_cliente(nome, idade, nif, email, morada, trabalho, data_nascimento, id_b)

            if code == 201:
                print("Cliente criado com sucesso.")
                print(obj)
            else:
                print("Erro:", obj)

        elif opcao == "2":
            code, obj = listar_clientes()

            if code == 200:
                for id_c, dados in obj.items():
                    print(f"ID: {id_c} | Nome: {dados['nome']} | Idade: {dados['idade']} | NIF: {dados['nif']} | Email: {dados['email']} | Trabalho: {dados['trabalho']} | Data Nascimento: {dados['data_nascimento']} | Bancário ID: {dados['bancario_id']}")
            else:
                print("Erro:", obj)

        elif opcao == "3":
            id_c = input("ID do cliente: ")
            code, obj = consultar_cliente(id_c)

            if code == 200:
                print(obj[id_c])
                print("Cliente consultado com sucesso.")
            else:
                print("Erro:", obj)

        elif opcao == "4":
            id_c = input("ID do cliente: ")

            nome = input("Novo nome (enter para manter): ")
            idade_str = input("Nova idade (enter para manter): ")
            nif = input("Novo NIF (enter para manter): ")
            email = input("Novo email (enter para manter): ")
            morada = input("Nova morada (enter para manter): ")
            trabalho = input("Novo trabalho (enter para manter): ")
            data_nascimento = input("Nova data nascimento YYYY-MM-DD (enter para manter): ")
            id_b = input("Novo ID bancário (enter para manter): ")

            if id_b and not bancario.existe_bancario(id_b):
                print("Erro: ID de bancário inválido.")
                continue

            code, obj = atualizar_cliente(
                id_c,
                nome if nome else None,
                int(idade_str) if idade_str else None,
                nif if nif else None,
                email if email else None,
                morada if morada else None,
                trabalho if trabalho else None,
                data_nascimento if data_nascimento else None,
                id_b if id_b else None
            )

            if code == 200:
                print("Cliente atualizado com sucesso.")
            else:
                print("Erro:", obj)

        elif opcao == "5":
            id_c = input("ID do cliente: ")
            code, obj = remover_cliente(id_c)

            if code == 200:
                print(obj)
            else:
                print("Erro:", obj)

        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


# ==============================
# BANCOS
# ==============================
def gerir_bancos():
    while True:
        menu_bancos()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do banco: ")
            nib = input("NIB (21 dígitos): ")
            email = input("Email: ")
            morada = input("Morada: ")
            telefone = input("Telefone: ")

            code, obj = criar_banco(nome, nib, email, morada, telefone)

            if code == 201:
                print("Banco criado com sucesso.")
                print(obj)
            else:
                print("Erro:", obj)

        elif opcao == "2":
            code, obj = listar_bancos()

            if code == 200:
                for id_bn, dados in obj.items():
                    print(f"ID: {id_bn} | Nome: {dados['nome']} | NIB: {dados['nib']} | Email: {dados['email']} | Morada: {dados['morada']} | Telefone: {dados['telefone']}")
            else:
                print("Erro:", obj)

        elif opcao == "3":
            id_bn = input("ID do banco: ")
            code, obj = consultar_banco(id_bn)

            if code == 200:
                print(obj[id_bn])
                print("Banco consultado com sucesso.")
            else:
                print("Erro:", obj)

        elif opcao == "4":
            id_bn = input("ID do banco: ")

            nome = input("Novo nome (enter para manter): ")
            nib = input("Novo NIB (enter para manter): ")
            email = input("Novo email (enter para manter): ")
            morada = input("Nova morada (enter para manter): ")
            telefone = input("Novo telefone (enter para manter): ")

            code, obj = atualizar_banco(
                id_bn,
                nome if nome else None,
                nib if nib else None,
                email if email else None,
                morada if morada else None,
                telefone if telefone else None
            )

            if code == 200:
                print("Banco atualizado com sucesso.")
            else:
                print("Erro:", obj)

        elif opcao == "5":
            id_bn = input("ID do banco: ")

            # Verificar se existem contas associadas antes de remover
            code_c, obj_c = listar_contas()
            if code_c == 200:
                associadas = [c for c in obj_c.values() if c["id_banco"] == id_bn]
                if associadas:
                    print(f"Erro: existem {len(associadas)} conta(s) associada(s) a este banco. Remova-as primeiro.")
                    continue

            code, obj = remover_banco(id_bn)

            if code == 200:
                print(obj)
            else:
                print("Erro:", obj)

        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


# ==============================
# CONTAS BANCÁRIAS
# ==============================
def gerir_contas():
    while True:
        menu_contas()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            code_c, _ = listar_clientes()
            if code_c != 200:
                print("Não existem clientes. Crie primeiro.")
                continue

            code_b, _ = listar_bancos()
            if code_b != 200:
                print("Não existem bancos. Crie primeiro.")
                continue

            id_c = input("ID do cliente: ")
            code_cc, _ = consultar_cliente(id_c)
            if code_cc != 200:
                print("Erro: ID de cliente inválido.")
                continue

            id_bn = input("ID do banco: ")
            if not existe_banco(id_bn):
                print("Erro: ID de banco inválido.")
                continue

            print("Tipo de conta: corrente / poupança")
            tipo = input("Tipo: ").strip().lower()
            saldo_str = input("Saldo inicial: ")

            try:
                saldo = float(saldo_str)
            except ValueError:
                print("Erro: saldo inválido.")
                continue

            code, obj = criar_conta(tipo, saldo, id_c, id_bn)

            if code == 201:
                print("Conta criada com sucesso.")
                print(obj)
            else:
                print("Erro:", obj)

        elif opcao == "2":
            code, obj = listar_contas()

            if code == 200:
                for id_ct, dados in obj.items():
                    print(f"ID: {id_ct} | Tipo: {dados['tipo']} | Saldo: {dados['saldo']:.2f}€ | Cliente ID: {dados['id_cliente']} | Banco ID: {dados['id_banco']}")
            else:
                print("Erro:", obj)

        elif opcao == "3":
            id_ct = input("ID da conta: ")
            code, obj = consultar_conta(id_ct)

            if code == 200:
                print(obj[id_ct])
                print("Conta consultada com sucesso.")
            else:
                print("Erro:", obj)

        elif opcao == "4":
            id_ct = input("ID da conta: ")

            tipo = input("Novo tipo corrente/poupança (enter para manter): ").strip().lower()
            saldo_str = input("Novo saldo (enter para manter): ")
            id_c = input("Novo ID cliente (enter para manter): ")
            id_bn = input("Novo ID banco (enter para manter): ")

            if id_c:
                from cliente import consultar_cliente as cc
                code_cc, _ = cc(id_c)
                if code_cc != 200:
                    print("Erro: ID de cliente inválido.")
                    continue

            if id_bn and not existe_banco(id_bn):
                print("Erro: ID de banco inválido.")
                continue

            saldo = None
            if saldo_str:
                try:
                    saldo = float(saldo_str)
                except ValueError:
                    print("Erro: saldo inválido.")
                    continue

            code, obj = atualizar_conta(
                id_ct,
                tipo if tipo else None,
                saldo,
                id_c if id_c else None,
                id_bn if id_bn else None
            )

            if code == 200:
                print("Conta atualizada com sucesso.")
            else:
                print("Erro:", obj)

        elif opcao == "5":
            id_ct = input("ID da conta: ")
            code, obj = remover_conta(id_ct)

            if code == 200:
                print(obj)
            else:
                print("Erro:", obj)

        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


# ==============================
# MAIN
# ==============================
def main():
    while True:
        menu_principal()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            gerir_bancarios()
        elif opcao == "2":
            gerir_clientes()
        elif opcao == "3":
            gerir_bancos()
        elif opcao == "4":
            gerir_contas()
        elif opcao == "0":
            print("A sair...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
