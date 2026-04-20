# ==============================
# main.py
# menu terminal para testar CRUD
# ==============================
import bancario
import cliente
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


# ==============================
# MENUS
# ==============================
def menu_principal():
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Gerir Bancários")
    print("2 - Gerir Clientes")
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


# ==============================
# GESTÃO DE BANCÁRIOS
# ==============================
def gerir_bancarios():
    while True:
        menu_bancarios()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome            = input("Nome: ")
            nif             = input("NIF: ")
            email           = input("Email: ")
            morada          = input("Morada: ")
            data_nascimento = input("Data nascimento (YYYY-MM-DD): ")
            code, obj = criar_bancario(nome, nif, email, morada, data_nascimento)
            if code == 201:
                print("Bancário criado com sucesso.")
                print(obj)
            else:
                print("Erro: " + obj)

        elif opcao == "2":
            code, obj = listar_bancarios()
            if code[0] == 200:
                for id_bancario, dados in obj.items():
                    print(
                        f"ID: {id_bancario} | Nome: {dados['nome']} | Idade: {dados['idade']} | NIF: {dados['nif']} | Email: {dados['email']} | Morada: {dados['morada']} | Data Nascimento: {dados['data_nascimento']}")
                print("Bancários listados com sucesso.")
            else:
                print("Erro: " + obj)

        elif opcao == "3":
            id_bancario = input("ID do bancário: ")
            code , obj = consultar_bancario(id_bancario)
            if code [0] == 200:
                print(obj[id_bancario])
                print("Bancário consultado com sucesso.")
            else:
                print("Erro: " + obj)

        elif opcao == "4":
            id_bancario = input("ID do bancário: ")
            nome            = input("Novo nome (enter para manter): ")
            nif             = input("Novo NIF (enter para manter): ")
            email           = input("Novo email (enter para manter): ")
            morada          = input("Nova morada (enter para manter): ")
            data_nascimento = input("Nova data nascimento YYYY-MM-DD (enter para manter): ")
            code , obj = atualizar_bancario(
                id_bancario,
                nome            if nome             else None,
                nif             if nif              else None,
                email           if email            else None,
                morada          if morada           else None,
                data_nascimento if data_nascimento  else None
            )
            if code [0] == 200:
                print("Bancário atualizado com sucesso.")
            else:
                print("Erro: " + obj)

        elif opcao == "5":
            id_bancario = input("ID do bancário: ")
            return_code = remover_bancario(id_bancario)
            if code [0] == 200:
                print("Bancário removido com sucesso.")
            else:
                print("Erro: " + obj )

        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


# ==============================
# GESTÃO DE CLIENTES
# ==============================
def gerir_clientes():
    while True:
        menu_clientes()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # listar bancários disponíveis antes de criar
            return_code = listar_bancarios()
            if return_code[0] != 200:
                print("Não existem bancários registados. Crie um bancário primeiro.")
                gerir_bancarios()
                continue
            id_bancario = input("ID do bancário responsável: ")
            if not bancario.existe_bancario(id_bancario):
                print("Erro: ID de bancário inválido.")
                continue
            nome            = input("Nome: ")
            idade           = int(input("Idade: "))
            nif             = input("NIF: ")
            email           = input("Email: ")
            morada          = input("Morada: ")
            trabalho        = input("Trabalho: ")
            data_nascimento = input("Data nascimento (YYYY-MM-DD): ")
            code, obj = criar_cliente(nome, idade, nif, email, morada, trabalho, data_nascimento, id_bancario)
            if code == 201:
                print("Cliente criado com sucesso.")
                print(obj)
            else:
                print("Erro: " + obj)

        elif opcao == "2":
            code, obj = listar_clientes()

            if code == 200:
                for id_cliente, dados in obj.items():
                    print(
                        f"ID: {id_cliente} | Nome: {dados['nome']} | Idade: {dados['idade']} | NIF: {dados['nif']} | Email: {dados['email']} | Trabalho: {dados['trabalho']} | Data Nascimento: {dados['data_nascimento']} | Bancário ID: {dados['bancario_id']}")
                print("Clientes listados com sucesso.")
            else:
                print("Erro: " + obj)

        elif opcao == "3":
            id_cliente = input("ID do cliente: ")
            code, obj = consultar_cliente(id_cliente)
            if code == 200:
                print(obj[id_cliente])
                print("Cliente consultado com sucesso.")
            else:
                print("Erro: " + obj)

        elif opcao == "4":
            id_cliente      = input("ID do cliente: ")
            nome            = input("Novo nome (enter para manter): ")
            idade_str       = input("Nova idade (enter para manter): ")
            nif             = input("Novo NIF (enter para manter): ")
            email           = input("Novo email (enter para manter): ")
            morada          = input("Nova morada (enter para manter): ")
            trabalho        = input("Novo trabalho (enter para manter): ")
            data_nascimento = input("Nova data nascimento YYYY-MM-DD (enter para manter): ")
            id_banc         = input("Novo ID bancário (enter para manter): ")
            if id_banc and not bancario.existe_bancario(id_banc):
                print("Erro: ID de bancário inválido.")
                continue
            return_code = atualizar_cliente(
                id_cliente,
                nome            if nome             else None,
                int(idade_str)  if idade_str        else None,
                nif             if nif              else None,
                email           if email            else None,
                morada          if morada           else None,
                trabalho        if trabalho         else None,
                data_nascimento if data_nascimento  else None,
                id_banc         if id_banc          else None
            )
            if return_code[0] == 200:
                print("Cliente atualizado com sucesso.")
            else:
                print("Erro: " + return_code[1])

        elif opcao == "5":
            id_cliente = input("ID do cliente: ")
            return_code = remover_cliente(id_cliente)
            if return_code[0] == 200:
                print("Cliente removido com sucesso.")
            else:
                print("Erro: " + return_code[1])

        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


# ==============================
# PROGRAMA PRINCIPAL
# ==============================
def main():
    while True:
        menu_principal()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            gerir_bancarios()
        elif opcao == "2":
            gerir_clientes()
        elif opcao == "0":
            print("A sair...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
