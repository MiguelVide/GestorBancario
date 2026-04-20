# ==============================
# cliente.py
# CRUD simples para entidade Cliente
# SEM utilização de classes
# armazenamento em dicionário
# validações feitas aqui (não no main)
# ==============================
from utils import gerar_id_cliente, validar_data, validar_nif, validar_email, validar_idade

clientes = {}


# CREATE
def criar_cliente(nome, idade, nif, email, morada, trabalho, data_nascimento, id_bancario):
    if not validar_data(data_nascimento):
        return 400, "Data inválida. Utilize formato YYYY-MM-DD."
    valido, msg = validar_idade(idade, data_nascimento)
    if not valido:
        return 400, msg
    if not validar_nif(nif):
        return 400, "NIF inválido. Deve conter 9 dígitos."
    if not validar_email(email):
        return 400, "Email inválido."
    id_cliente = gerar_id_cliente()
    cliente = {
        "nome": nome,
        "idade": idade,
        "nif": nif,
        "email": email,
        "morada": morada,
        "trabalho": trabalho,
        "data_nascimento": data_nascimento,
        "bancario_id": id_bancario
    }
    clientes[id_cliente] = cliente
    return 201, cliente


# READ (listar todos)
def listar_clientes():
    if not clientes:
        print("Não existem clientes registados.")
        return 404, "Não existem clientes registados."
    return 200, clientes


# READ (consultar individual)
def consultar_cliente(id_cliente):
    if id_cliente not in clientes:
        print("Cliente não encontrado.")
        return 404, "Cliente não encontrado."

    return 200, clientes[id_cliente]


# UPDATE
def atualizar_cliente(id_cliente, nome=None, idade=None, nif=None, email=None, morada=None, trabalho=None, data_nascimento=None, id_bancario=None):
    if id_cliente not in clientes:
        print("Cliente não encontrado.")
        return 404, "Cliente não encontrado."
    if data_nascimento:
        if not validar_data(data_nascimento):
            print("Data inválida. Utilize formato YYYY-MM-DD.")
            return 400, "Data inválida. Utilize formato YYYY-MM-DD."
        clientes[id_cliente]["data_nascimento"] = data_nascimento
    if idade:
        data_nasc_atual = clientes[id_cliente]["data_nascimento"]
        valido, msg = validar_idade(idade, data_nasc_atual)
        if not valido:
            print(msg)
            return 400, msg
        clientes[id_cliente]["idade"] = idade
    if nif:
        if not validar_nif(nif):
            print("NIF inválido. Deve conter 9 dígitos.")
            return 400, "NIF inválido. Deve conter 9 dígitos."
        clientes[id_cliente]["nif"] = nif
    if email:
        if not validar_email(email):
            print("Email inválido.")
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
    print("Cliente atualizado com sucesso.")
    return 200, clientes[id_cliente]


# DELETE
def remover_cliente(id_cliente):
    if id_cliente not in clientes:
        print("Cliente não encontrado.")
        return 404, "Cliente não encontrado."
    del clientes[id_cliente]
    print("Cliente removido com sucesso.")
    return 200, id_cliente
