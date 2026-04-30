from datetime import datetime, date

contador_bancarios = 1
contador_clientes = 1
contador_bancos = 1
contador_contas = 1


def gerar_id_bancario():
    global contador_bancarios
    novo_id = f"B{contador_bancarios:03d}"
    contador_bancarios += 1
    return novo_id


def gerar_id_cliente():
    global contador_clientes
    novo_id = f"C{contador_clientes:03d}"
    contador_clientes += 1
    return novo_id


def gerar_id_banco():
    global contador_bancos
    novo_id = f"BN{contador_bancos:03d}"
    contador_bancos += 1
    return novo_id


def gerar_id_conta():
    global contador_contas
    novo_id = f"CT{contador_contas:03d}"
    contador_contas += 1
    return novo_id


def validar_data(data_texto):
    try:
        datetime.strptime(data_texto, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validar_nif(nif):
    return isinstance(nif, str) and nif.isdigit() and len(nif) == 9


def validar_email(email):
    partes = email.split("@")
    return len(partes) == 2 and "." in partes[1] and len(partes[1]) > 2


def validar_idade(idade, data_nascimento):
    ano, mes, dia = map(int, data_nascimento.split("-"))

    hoje = date.today()
    idade_calc = hoje.year - ano - ((hoje.month, hoje.day) < (mes, dia))

    if idade < 18:
        return False, "Menor de idade. Apenas maiores de 18 anos são permitidos."

    if idade != idade_calc:
        return False, f"Idade ({idade}) não corresponde à data de nascimento ({idade_calc})."

    return True, ""
