# ==============================
# Funções de validação e cálculo
# ==============================

from datetime import datetime, date

# Validação de idade e data de nascimento
def validar_idade(idade, data_nascimento):
    ano, mes, dia = map(int, data_nascimento.split("-"))
    idade_calc = date.today().year - ano - ((date.today().month, date.today().day) < (mes, dia))
    if idade < 18:
        return False, "❌ Menor de idade. Apenas maiores de 18 anos são permitidos."
    if idade != idade_calc:
        return False, f"❌ Idade ({idade}) não bate com a data de nascimento ({idade_calc})."
    return True, ""

def validar_nif(nif):
    if isinstance(nif,str) and nif.isdigit() and len(nif)==9:
        return True, ""
    return False, "❌ NIF inválido."

def validar_email(email):
    if "@" in email and "." in email:
        return True, ""
    return False, "❌ Email inválido."

def validar_data(data):
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True, ""
    except:
        return False, "❌ Data inválida, use YYYY-MM-DD."

def calcular_idade(data_nascimento):
    ano, mes, dia = map(int, data_nascimento.split("-"))
    idade_calc = date.today().year - ano - ((date.today().month, date.today().day) < (mes, dia))
    return idade_calc