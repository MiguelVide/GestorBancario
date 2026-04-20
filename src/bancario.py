# ==============================
# bancario.py
# CRUD simples para entidade Bancário
# SEM utilização de classes
# armazenamento em dicionário
# validações feitas aqui (não no main)
# ==============================
from utils import gerar_id_bancario, validar_data, validar_nif, validar_email, validar_idade

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
        "nome": nome,
        "nif": nif,
        "email": email,
        "morada": morada,
        "data_nascimento": data_nascimento
    }
    bancarios[id_bancario] = bancario
    print(f"Bancário criado com sucesso. ID: {id_bancario}")
    return 201, bancario


# READ (listar todos)
def listar_bancarios():
    if not bancarios:
        print("Não existem bancários registados.")
        return 404, "Não existem bancários registados."
    return 200, bancarios


# READ (consultar individual)
def consultar_bancario(id_bancario):
    if id_bancario not in bancarios:
        print("Bancário não encontrado.")
        return 404, "Bancário não encontrado."
    return 200, bancarios[id_bancario]


# UPDATE
def atualizar_bancario(id_bancario, nome=None, idade=None, nif=None, email=None, morada=None, data_nascimento=None):
    if id_bancario not in bancarios:
        print("Bancário não encontrado.")
        return 404, atualizar_bancario
    if data_nascimento:
        if not validar_data(data_nascimento):
            print("Data inválida. Utilize formato YYYY-MM-DD.")
            return 400, "Data inválida. Utilize formato YYYY-MM-DD."
        bancarios[id_bancario]["data_nascimento"] = data_nascimento
    if idade:
        data_nasc_atual = bancarios[id_bancario]["data_nascimento"]
        valido, msg = validar_idade(idade, data_nasc_atual)
        if not valido:
            print(msg)
            return 400, msg
        bancarios[id_bancario]["idade"] = idade
    if nif:
        if not validar_nif(nif):
            print("NIF inválido. Deve conter 9 dígitos.")
            return 400, "NIF inválido. Deve conter 9 dígitos."
        bancarios[id_bancario]["nif"] = nif
    if email:
        if not validar_email(email):
            print("Email inválido.")
            return 400, "Email inválido."
        bancarios[id_bancario]["email"] = email
    if nome:
        bancarios[id_bancario]["nome"] = nome
    if morada:
        bancarios[id_bancario]["morada"] = morada
    print("Bancário atualizado com sucesso.")
    return 200, bancarios[id_bancario]


# DELETE
def remover_bancario(id_bancario):
    if id_bancario not in bancarios:
        print("Bancário não encontrado.")
        return 404, remover_bancario
    del bancarios[id_bancario]
    print("Bancário removido com sucesso.")
    return 200, remover_bancario


# AUXILIAR
def existe_bancario(id_bancario):
    return id_bancario in bancarios