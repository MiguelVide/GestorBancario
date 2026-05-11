import json
import os

from utils import (
    gerar_id_cliente,
    validar_data,
    validar_nif,
    validar_email
)

FICHEIRO_CLIENTES = "clientes.json"

clientes = {}


# ==========================
# Persistência
# ==========================
def guardar_clientes():
    with open(FICHEIRO_CLIENTES, "w", encoding="utf-8") as ficheiro:
        json.dump(clientes, ficheiro, indent=4, ensure_ascii=False)


def carregar_clientes():
    global clientes

    if os.path.exists(FICHEIRO_CLIENTES):
        with open(FICHEIRO_CLIENTES, "r", encoding="utf-8") as ficheiro:
            clientes = json.load(ficheiro)
    else:
        clientes = {}


# CREATE
def criar_cliente(nome, nif, email, morada, trabalho, data_nascimento, id_bancario):
    carregar_clientes()

    if not validar_data(data_nascimento):
        return 400, "Data inválida. Utilize formato YYYY-MM-DD."

    if not validar_nif(nif):
        return 400, "NIF inválido. Deve conter 9 dígitos."

    if not validar_email(email):
        return 400, "Email inválido."

    id_cliente = gerar_id_cliente()

    cliente = {
        "id": id_cliente,
        "nome": nome,
        "nif": nif,
        "email": email,
        "morada": morada,
        "trabalho": trabalho,
        "data_nascimento": data_nascimento,
        "bancario_id": id_bancario
    }

    clientes[id_cliente] = cliente
    guardar_clientes()
    return 201, cliente


# READ
def listar_clientes():
    carregar_clientes()

    if not clientes:
        return 404, "Não existem clientes registados."
    return 200, clientes


def consultar_cliente(id_cliente):
    carregar_clientes()

    if id_cliente not in clientes:
        return 404, "Cliente não encontrado."
    return 200, {id_cliente: clientes[id_cliente]}


# UPDATE
def atualizar_cliente(
    id_cliente,
    nome=None,
    nif=None,
    email=None,
    morada=None,
    trabalho=None,
    data_nascimento=None,
    id_bancario=None
):
    carregar_clientes()

    if id_cliente not in clientes:
        return 404, "Cliente não encontrado."

    if data_nascimento:
        if not validar_data(data_nascimento):
            return 400, "Data inválida. Utilize formato YYYY-MM-DD."

        clientes[id_cliente]["data_nascimento"] = data_nascimento

    if nif:
        if not validar_nif(nif):
            return 400, "NIF inválido. Deve conter 9 dígitos."

        clientes[id_cliente]["nif"] = nif

    if email:
        if not validar_email(email):
            return 400, "Email inválido."

        clientes[id_cliente]["email"] = email

    if nome:
        clientes[id_cliente]["nome"] = nome

    if morada:
        clientes[id_cliente]["morada"] = morada

    if trabalho:
        clientes[id_cliente]["trabalho"] = trabalho

    if id_bancario:
        clientes[id_cliente]["bancario_id"] = id_bancario

    guardar_clientes()
    return 200, clientes[id_cliente]


# DELETE
def remover_cliente(id_cliente):
    carregar_clientes()

    if id_cliente not in clientes:
        return 404, "Cliente não encontrado."

    del clientes[id_cliente]
    guardar_clientes()

    return 200, f"Cliente {id_cliente} removido."
