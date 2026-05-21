import json
import os

from utils import gerar_id_conta, validar_tipo_conta, logger

FICHEIRO_CONTAS = "contas.json"

contas = {}


# ==========================
# Persistência
# ==========================
def guardar_contas():
    with open(FICHEIRO_CONTAS, "w", encoding="utf-8") as ficheiro:
        json.dump(contas, ficheiro, indent=4, ensure_ascii=False)


def carregar_contas():
    global contas

    if os.path.exists(FICHEIRO_CONTAS):
        with open(FICHEIRO_CONTAS, "r", encoding="utf-8") as ficheiro:
            contas = json.load(ficheiro)
    else:
        contas = {}


# CREATE
def criar_conta(tipo, saldo_inicial, id_cliente, id_banco):
    carregar_contas()

    if not validar_tipo_conta(tipo):
        logger.error(f"Tentativa de criar conta com tipo inválido: '{tipo}'")
        return 400, "Tipo de conta inválido. Use 'corrente' ou 'poupança'."

    if not isinstance(saldo_inicial, (int, float)) or saldo_inicial < 0:
        logger.error(f"Tentativa de criar conta com saldo inválido: '{saldo_inicial}'")
        return 400, "Saldo inicial inválido. Deve ser um valor numérico não negativo."

    id_conta = gerar_id_conta()

    conta = {
        "id": id_conta,
        "tipo": tipo,
        "saldo": saldo_inicial,
        "id_cliente": id_cliente,
        "id_banco": id_banco
    }

    contas[id_conta] = conta
    guardar_contas()
    logger.info(f"Conta criada: ID={id_conta} | Tipo={tipo} | Saldo={saldo_inicial} | Cliente={id_cliente} | Banco={id_banco}")
    return 201, conta


# READ
def listar_contas():
    carregar_contas()

    if not contas:
        logger.debug("Listagem de contas: nenhum registo encontrado.")
        return 404, "Não existem contas registadas."
    logger.debug(f"Listagem de contas: {len(contas)} registo(s) encontrado(s).")
    return 200, contas


def consultar_conta(id_conta):
    carregar_contas()

    if id_conta not in contas:
        logger.warning(f"Consulta de conta falhou: ID '{id_conta}' não encontrado.")
        return 404, "Conta não encontrada."
    logger.info(f"Conta consultada: ID={id_conta}")
    return 200, {id_conta: contas[id_conta]}


# UPDATE
def atualizar_conta(id_conta, tipo=None, saldo=None, id_cliente=None, id_banco=None):
    carregar_contas()

    if id_conta not in contas:
        logger.warning(f"Tentativa de atualizar conta inexistente: ID '{id_conta}'")
        return 404, "Conta não encontrada."

    # Validar tudo antes de guardar
    if tipo and not validar_tipo_conta(tipo):
        logger.error(f"Atualização de conta ID={id_conta}: tipo inválido '{tipo}'")
        return 400, "Tipo de conta inválido. Use 'corrente' ou 'poupança'."

    if saldo is not None:
        if not isinstance(saldo, (int, float)) or saldo < 0:
            logger.error(f"Atualização de conta ID={id_conta}: saldo inválido '{saldo}'")
            return 400, "Saldo inválido. Deve ser um valor numérico não negativo."

    # Aplicar alterações
    if tipo:
        contas[id_conta]["tipo"] = tipo
    if saldo is not None:
        contas[id_conta]["saldo"] = saldo
    if id_cliente:
        contas[id_conta]["id_cliente"] = id_cliente
    if id_banco:
        contas[id_conta]["id_banco"] = id_banco

    guardar_contas()
    logger.info(f"Conta atualizada: ID={id_conta}")
    return 200, contas[id_conta]


# DELETE
def remover_conta(id_conta):
    carregar_contas()

    if id_conta not in contas:
        logger.warning(f"Tentativa de remover conta inexistente: ID '{id_conta}'")
        return 404, "Conta não encontrada."

    del contas[id_conta]
    guardar_contas()
    logger.info(f"Conta removida: ID={id_conta}")
    return 200, {id_conta}


# AUX
def existe_conta(id_conta):
    carregar_contas()
    return id_conta in contas
