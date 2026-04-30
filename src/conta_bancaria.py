from utils import gerar_id_conta

contas = {}


# CREATE
def criar_conta(tipo, saldo_inicial, id_cliente, id_banco):
    if not validar_tipo_conta(tipo):
        return 400, "Tipo de conta inválido. Use 'corrente' ou 'poupança'."

    if not isinstance(saldo_inicial, (int, float)) or saldo_inicial < 0:
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
    return 201, conta


# READ
def listar_contas():
    if not contas:
        return 404, "Não existem contas registadas."
    return 200, contas


def consultar_conta(id_conta):
    if id_conta not in contas:
        return 404, "Conta não encontrada."
    return 200, {id_conta: contas[id_conta]}


# UPDATE
def atualizar_conta(id_conta, tipo=None, saldo=None, id_cliente=None, id_banco=None):
    if id_conta not in contas:
        return 404, "Conta não encontrada."

    # Validar tudo antes de guardar
    if tipo and not validar_tipo_conta(tipo):
        return 400, "Tipo de conta inválido. Use 'corrente' ou 'poupança'."

    if saldo is not None:
        if not isinstance(saldo, (int, float)) or saldo < 0:
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

    return 200, contas[id_conta]


# DELETE
def remover_conta(id_conta):
    if id_conta not in contas:
        return 404, "Conta não encontrada."

    del contas[id_conta]
    return 200, f"Conta {id_conta} removida."


# AUX
def existe_conta(id_conta):
    return id_conta in contas


def validar_tipo_conta(tipo):
    return tipo in ("corrente", "poupança")