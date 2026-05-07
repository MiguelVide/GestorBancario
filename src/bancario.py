from utils import gerar_id_bancario, validar_data, validar_nif, validar_email

bancarios = {}

# CREATE
def criar_bancario(nome, nif, email, morada, data_nascimento):
    if not validar_data(data_nascimento):
        return 400, "Data inválida. Utilize formato YYYY-MM-DD."
    if not validar_nif(nif):
        return 400, "NIF inválido. Deve conter 9 dígitos."
    if not validar_email(email):
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
    return 201, bancario


# READ
def listar_bancarios():
    if not bancarios:
        return 404, "Não existem bancários registados."
    return 200, bancarios


def consultar_bancario(id_bancario):
    if id_bancario not in bancarios:
        return 404, "Bancário não encontrado."
    return 200, {id_bancario: bancarios[id_bancario]}


# UPDATE
def atualizar_bancario(id_bancario, nome=None, nif=None, email=None, morada=None, data_nascimento=None):
    if id_bancario not in bancarios:
        return 404, "Bancário não encontrado."

    if data_nascimento:
        if not validar_data(data_nascimento):
            return 400, "Data inválida. Utilize formato YYYY-MM-DD."
        bancarios[id_bancario]["data_nascimento"] = data_nascimento

    if nif:
        if not validar_nif(nif):
            return 400, "NIF inválido. Deve conter 9 dígitos."
        bancarios[id_bancario]["nif"] = nif

    if email:
        if not validar_email(email):
            return 400, "Email inválido."
        bancarios[id_bancario]["email"] = email

    if nome:
        bancarios[id_bancario]["nome"] = nome

    if morada:
        bancarios[id_bancario]["morada"] = morada

    return 200, bancarios[id_bancario]


# DELETE
def remover_bancario(id_bancario):
    if id_bancario not in bancarios:
        return 404, "Bancário não encontrado."

    del bancarios[id_bancario]
    return 200, f"Bancário {id_bancario} removido."


# AUX
def existe_bancario(id_bancario):
    return id_bancario in bancarios
