import json
import os

from utils import gerar_id_bancario, validar_data, validar_nif, validar_email, logger

FICHEIRO_BANCARIOS = "bancarios.json"

bancarios = {}


# ==========================
# Persistência
# ==========================
def guardar_bancarios():
    with open(FICHEIRO_BANCARIOS, "w", encoding="utf-8") as ficheiro:
        json.dump(bancarios, ficheiro, indent=4, ensure_ascii=False)


def carregar_bancarios():
    global bancarios

    if os.path.exists(FICHEIRO_BANCARIOS):
        with open(FICHEIRO_BANCARIOS, "r", encoding="utf-8") as ficheiro:
            bancarios = json.load(ficheiro)
    else:
        bancarios = {}


# CREATE
def criar_bancario(nome, nif, email, morada, data_nascimento):
    carregar_bancarios()

    if not validar_data(data_nascimento):
        logger.error(f"Tentativa de criar bancário com data inválida: '{data_nascimento}'")
        return 400, "Data inválida. Utilize formato YYYY-MM-DD."
    if not validar_nif(nif):
        logger.error(f"Tentativa de criar bancário com NIF inválido: '{nif}'")
        return 400, "NIF inválido. Deve conter 9 dígitos."
    if not validar_email(email):
        logger.error(f"Tentativa de criar bancário com email inválido: '{email}'")
        return 400, "Email inválido."

    id_bancario = gerar_id_bancario()

    bancario = {
        "id": id_bancario,
        "nome": nome,
        "nif": nif,
        "email": email,
        "morada": morada,
        "data_nascimento": data_nascimento
    }

    bancarios[id_bancario] = bancario
    guardar_bancarios()
    logger.info(f"Bancário criado: ID={id_bancario} | Nome={nome} | Email={email}")
    return 201, bancario


# READ
def listar_bancarios():
    carregar_bancarios()

    if not bancarios:
        logger.debug("Listagem de bancários: nenhum registo encontrado.")
        return 404, "Não existem bancários registados."
    logger.debug(f"Listagem de bancários: {len(bancarios)} registo(s) encontrado(s).")
    return 200, bancarios


def consultar_bancario(id_bancario):
    carregar_bancarios()

    if id_bancario not in bancarios:
        logger.warning(f"Consulta de bancário falhou: ID '{id_bancario}' não encontrado.")
        return 404, "Bancário não encontrado."
    logger.info(f"Bancário consultado: ID={id_bancario}")
    return 200, {id_bancario: bancarios[id_bancario]}


# UPDATE
def atualizar_bancario(id_bancario, nome=None, nif=None, email=None, morada=None, data_nascimento=None):
    carregar_bancarios()

    if id_bancario not in bancarios:
        logger.warning(f"Tentativa de atualizar bancário inexistente: ID '{id_bancario}'")
        return 404, "Bancário não encontrado."

    if data_nascimento:
        if not validar_data(data_nascimento):
            logger.error(f"Atualização de bancário ID={id_bancario}: data inválida '{data_nascimento}'")
            return 400, "Data inválida. Utilize formato YYYY-MM-DD."
        bancarios[id_bancario]["data_nascimento"] = data_nascimento

    if nif:
        if not validar_nif(nif):
            logger.error(f"Atualização de bancário ID={id_bancario}: NIF inválido '{nif}'")
            return 400, "NIF inválido. Deve conter 9 dígitos."
        bancarios[id_bancario]["nif"] = nif

    if email:
        if not validar_email(email):
            logger.error(f"Atualização de bancário ID={id_bancario}: email inválido '{email}'")
            return 400, "Email inválido."
        bancarios[id_bancario]["email"] = email

    if nome:
        bancarios[id_bancario]["nome"] = nome

    if morada:
        bancarios[id_bancario]["morada"] = morada

    guardar_bancarios()
    logger.info(f"Bancário atualizado: ID={id_bancario}")
    return 200, bancarios[id_bancario]


# DELETE
def remover_bancario(id_bancario):
    carregar_bancarios()

    if id_bancario not in bancarios:
        logger.warning(f"Tentativa de remover bancário inexistente: ID '{id_bancario}'")
        return 404, "Bancário não encontrado."

    del bancarios[id_bancario]
    guardar_bancarios()
    logger.info(f"Bancário removido: ID={id_bancario}")
    return 200, f"Bancário {id_bancario} removido."


# AUX
def existe_bancario(id_bancario):
    carregar_bancarios()
    return id_bancario in bancarios
