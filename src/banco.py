from utils import gerar_id_banco, validar_email

bancos = {}


# CREATE
def criar_banco(nome, email, morada, telefone):

    if not validar_email(email):
        return 400, "Email inválido."

    if any(b["email"] == email for b in bancos.values()):
        return 409, "Email já registado."

    id_banco = gerar_id_banco()

    banco = {
        "id": id_banco,
        "nome": nome,
        "email": email,
        "morada": morada,
        "telefone": telefone
    }

    bancos[id_banco] = banco
    return 201, banco


# READ
def listar_bancos():
    if not bancos:
        return 404, "Não existem bancos registados."
    return 200, bancos


def consultar_banco(id_banco):
    if id_banco not in bancos:
        return 404, "Banco não encontrado."
    return 200, {id_banco: bancos[id_banco]}


# UPDATE
def atualizar_banco(id_banco, nome=None, email=None, morada=None, telefone=None):

    if id_banco not in bancos:
        return 404, "Banco não encontrado."

    if email:
        if not validar_email(email):
            return 400, "Email inválido."

        if any(b["email"] == email and b["id"] != id_banco for b in bancos.values()):
            return 409, "Email já registado."

    if nome:
        bancos[id_banco]["nome"] = nome

    if email:
        bancos[id_banco]["email"] = email

    if morada:
        bancos[id_banco]["morada"] = morada

    if telefone:
        bancos[id_banco]["telefone"] = telefone

    return 200, bancos[id_banco]


# DELETE
def remover_banco(id_banco):

    if id_banco not in bancos:
        return 404, "Banco não encontrado."

    del bancos[id_banco]

    return 200, f"Banco {id_banco} removido."


# AUX
def existe_banco(id_banco):
    return id_banco in bancos
